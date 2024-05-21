import requests
from bs4 import BeautifulSoup
import json
import schedule
import time


class ZDFScraper:
    def __init__(self):
        self.base_url = "https://www.zdf.de/nachrichten"
        self.last_article_count = 0

    def scrape(self):
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, "html.parser")
        news_links = [link["href"] for link in soup.select("div.i13b5qgu a")]
        article_count = len(news_links)

        if article_count > self.last_article_count:
            new_articles = article_count - self.last_article_count
            print(f"{new_articles} new articles found!")
            self.last_article_count = article_count
            all_news = []
            for link in news_links:
                news = self.extract_news(link)
                all_news.append(news)

            with open("ZDF_dataset_2.json", "w", encoding="utf-8") as f:
                json.dump(all_news, f, ensure_ascii=False, indent=4)

    def extract_news(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        news = {
            "Link": url,
            "News Category": [category.get_text(strip=True) for category in soup.select("span.o1byiadb.t1ktg2ut")],
            "Author": [author.get_text(strip=True) for author in soup.select("span.m211382")],
            "publish_time": [time.get_text(strip=True) for time in soup.select("span.djkus7a.m211382")],
            "Title": [title.get_text(strip=True) for title in soup.select("span.t1w1kov8.hhhtovw")],
            "scribe": [scribe.get_text(strip=True) for scribe in soup.select("p.ikh9v7p.c1bdz7f4")],
            "Text": [text.get_text(strip=True) for text in soup.select("div.s1am5zo.f1uhhdhr")]
        }
        return news


# Beispielaufruf
scraper = ZDFScraper()

# Schedule einrichten

schedule.every(1).minutes.do(scraper.scrape)

while True:
    schedule.run_pending()
    print(time.localtime())
    time.sleep(20)
