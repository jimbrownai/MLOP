import requests
from bs4 import BeautifulSoup


def scrape_marketWatch(limit):
    # Feeds market watch is in XML Format | Using XML parser
    url = "https://feeds.marketwatch.com/marketwatch/topstories/"
    HEADERS = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) ")}

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "xml")

    headline = [] 
    for item in soup.find_all("item")[:10]:
        headline.append(item.title.get_text())

    return headline

def scrape_benzinga(limit):
    url = "https://www.benzinga.com/news/"
    HEADERS = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) ")}
    response = requests.get(url)
    headline = []

    #DOM Structure <div class=content-feed-list><div class=newsfeed-card><div class=post-card-feed>
    soup = BeautifulSoup(response.text,'html.parser')
    articles = soup.find_all("div", class_="newsfeed-card")[:limit]
    for article in articles: 
        title = article.find("div", class_="post-card-feed")
        headline.append(title)
        # print(title.get_text())
        # print("***************************************")

# container__headline-text

urls = [
        # "https://finviz.com/news.ashx",
        # "https://finance.yahoo.com/markets/stocks/trending/",
        # "https://www.benzinga.com/news/",
        "https://edition.cnn.com/business",
        # "https://www.investing.com/news/stock-market-news",
        # "https://www.cnbc.com/markets/",
        # "https://www.reuters.com/markets/"
        ]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0 Safari/537.36"
    )
}
for url in urls :
    response = requests.get(url)
    if response.status_code == 200:
        # print(response,url) newsfeed-card
        soup = BeautifulSoup(response.text,'html.parser')
        # articles = soup.find_all("div", class_="content-feed-list")

        articles = soup.find_all("span", class_="container__headline-text")
        # print(articles)
        for article in articles: 
            print(article.get_text())
            print("***************************************")
#         # news = [] 
#         # for h3 in soup.select("article", class_="news-card")[:5]:
#         #     title = h3.get_text()
#         #     news.append(title)
#         # print(news)
#         # news = [] 

