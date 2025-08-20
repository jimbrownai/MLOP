import requests
from bs4 import BeautifulSoup


def scrap_marketWatch(limit):
    # Feeds market watch is in XML Format | Using XML parser
    url = "https://feeds.marketwatch.com/marketwatch/topstories/"
    HEADERS = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) ")}

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "xml")

    headline = [] 
    for item in soup.find_all("item")[:10]:
        headline.append(item.title.get_text())

    return headline

print(scrap_marketWatch(5))