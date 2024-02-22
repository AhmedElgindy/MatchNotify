import requests
from bs4 import BeautifulSoup


class HtmlContent:

    def __init__(self, url):
        self.__url = url
        self.soup = self.getContent()

    def getUrl(self) -> str:
        return self.__url

    def getContent(self) -> str:
        try:
            response = requests.get(self.getUrl())
            response.raise_for_status()
            return BeautifulSoup(response.content, "html.parser")

        except requests.RequestException as e:
            print(f"there is error to get data{e}")
            return None


# this class used the HtmlContent class to filter the soup
# I did that to make the class more resuable
class SportData:
    def __init__(self, htmlContent: HtmlContent) -> None:
        """
        Get the soup from htmlContent from the htmlContent class

        """
        self.soup = htmlContent.soup

    def get_match_data(self) -> dict:
        """
        Get all match data including championships, teams, and times.

        Returns:
            dict: A dictionary containing match data organized by championship.
                Keys are championship names and values are lists of dictionaries, # noqa
                where each dictionary represents a match with keys 'teamA', 'teamB',
                and 'time'.
        """
        match_data = {}
        if not self.soup:
            return []
        self.matchCards = self.soup.find_all("div", {"class", "matchesList"})
        for i, matchCard in enumerate(self.matchCards):
            try:
                championship = (
                    matchCard.find("div", {"class", "title"})
                    .find("h2")
                    .text.strip()  # noqa
                )
            except AttributeError:
                # Handle the case where the championship title cannot be found
                championship = f"Unknown Championship {i + 1}"

            teams = matchCard.find("div", {"class": "ul"}).find_all(
                "div", {"class": "liItem"}
            )
            matches = []
            for team in teams:
                teamA = (
                    team.find("div", {"class": "teamA"}).find("p").text.strip()
                )  # noqa
                teamB = (
                    team.find("div", {"class": "teamB"}).find("p").text.strip()
                )  # noqa
                time_element = team.find("span", {"class": "time"})
                time = time_element.text.strip() if time_element else ""
                matches.append({"teamA": teamA, "teamB": teamB, "time": time})
            if championship in match_data:
                match_data[championship].extend(matches)
            else:
                match_data[championship] = matches
        return match_data


# url ="https://www.yallakora.com/match-center/مركز-المباريات?date=2/29/2024"
