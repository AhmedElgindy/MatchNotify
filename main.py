from scraping import HtmlContent, SportData
from notification import Notification
from utils import get_current_date, importantMatches


def main():
    current_date = get_current_date()
    html = HtmlContent(
        # here you can use any date for me I used the current date
        f"https://www.yallakora.com/match-center/مركز-المباريات?date={current_date}"  # noqa
    )
    sportobj = SportData(html)
    matchDatas = sportobj.get_match_data()
    for championship in matchDatas:
        """we filter out the dict to give use teh important matches that we need # noqa
        here you can go to importantMatches dit and modify it as you want
        you can add any sport into the list or you can display all of
        the matchs"""

        if championship in importantMatches:
            for matchdata in matchDatas[championship]:
                # Get the data we want and create our message
                teamA = matchdata["teamA"]
                teamB = matchdata["teamB"]
                time = matchdata["time"]

                message = f" ماتش اليوم الساعة {time} بين {teamA} و {teamB} "
                # create my notification object the will be displayed
                notification = Notification(
                    title=championship,
                    message=message,
                    urgency="critical",
                    timeout=5,
                    icon=importantMatches[championship],  # noqa
                )  # noqa
                # displaying the match
                notification.send()


main()
