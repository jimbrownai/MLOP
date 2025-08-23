import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd


def scrape_marketWatch(limit):
    # Feeds market watch is in XML Format | Using XML parser
    url = "https://feeds.marketwatch.com/marketwatch/topstories/"
    HEADERS = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) ")}
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "xml")
    headlines = []

    for item in soup.find_all("item")[:10]:
        headlines.append(item.title.get_text())
    return headlines

def scrape_benzinga(limit):
    url = "https://www.benzinga.com/news/"
    HEADERS = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) ")}
    response = requests.get(url)
    headlines = []
    #DOM Structure <div class=content-feed-list><div class=newsfeed-card><div class=post-card-feed>
    soup = BeautifulSoup(response.text,'html.parser')
    articles = soup.find_all("div", class_="newsfeed-card")[:limit]
    for article in articles: 
        title = article.find("div", class_="post-card-feed")
        headlines.append(title.get_text())
    return headlines

def scrape_edition_cnn(limit):
    url = "https://edition.cnn.com/business"
    HEADERS = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) ")}
    response = requests.get(url)
    headlines = []
    soup = BeautifulSoup(response.text,'html.parser')
    articles = soup.find_all("div", class_="container__text container_lead-plus-headlines__text")[:limit]
    for article in articles:
        data = article.find("span", class_="container__headline-text")
        headlines.append(data.get_text())
    return headlines



def fetch_page(url, retries=3):
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0 Safari/537.36"
        )}
    for attempt in range(3):
        try:
            response = requests.get(url, headers=HEADERS,timeout=10)
            if response.status_code in [403,401]:
                time.sleep(2**attempt + random.random())
                continue
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            time.sleep(2** attempt+random.random())
    return None

def scrape_site(url,limit):
    #common structure without ref any class names to scrape
    response = fetch_page(url)
    if not response:
        return 
    soup = BeautifulSoup(response,"html.parser")
    titles = [t.get_text(strip=True) for t in soup.select("a")]
    headlines = [] 
    for idx, title in enumerate(titles, 1):
        if len(title)>40: 
            # print(f"{idx}. {title}")
            headlines.append(title)
    return headlines[:limit]

def get_headlines(limit):
    res = scrape_site("https://www.cnbc.com/",limit) + scrape_marketWatch(limit) + scrape_edition_cnn(limit) + scrape_benzinga(limit)
    return res

def save_headlines_to_file(limit):
    res = get_headlines(limit)
    d = {'headlines':res}
    df = pd.DataFrame(d)
    # print(df.head(5))
    df.to_csv("headlines.csv",index=False)

def save_stock_tickers_info():
    headers = {"User-Agent": "Mozilla/5.0"}
    datalist = [] 
    for i in range(1,5):
        url = (
            "https://stockanalysis.com/api/screener/s/f"
            "?m=marketCap&s=desc&c=no,s,n,marketCap,price,change,revenue"
            "&sc=marketCap&cn=500&f=exchange-is-NYSE"
            f"&p={i}&i=stocks"
        )
        response = requests.get(url, headers=headers)
        tree = response.json()
        datalist = datalist+(tree['data']['data'])
    df = pd.DataFrame(datalist)
    df.columns = ["Rank", "Symbol", "Company", "MarketCap", "Price", "Change", "Revenue"]
    df.to_csv('ticker_info.csv',index=False)

def main():
    
    save_stock_tickers_info()

if __name__ =='__main__':
    main()