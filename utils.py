from datetime import datetime


def get_current_date():
    # Get the current date and format it as "month/day/year"
    current_date = datetime.now().strftime("%m/%d/%Y")
    return current_date


importantMatches = {
    "كأس ملك أسبانيا": "icons/spanishCup.png",
    "الدوري المصري": "icons/egyption.png",
    "كأس الاتحاد الإنجليزي": "icons/englishCup.png",
    "الدوري الإنجليزي": "icons/english.png",
    "الدوري الإسباني": "icons/spanish.png",
    "دوري أبطال إفريقيا": "icons/caf.jpg",
    "الدوري الأوروبي": "icons/Europa.png",
    "دوري أبطال أوروبا": "icons/UEFA.png",
}
