import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json
import schedule
import time


last_article_count = 0

visited_scraped_all_links = []


start_url = "https://www.zdf.de/nachrichten"
response = requests.get(start_url)
soup = BeautifulSoup(response.content, "html.parser")


def extract_news(url):
    new_response = requests.get(link_to_news)
    new_soup = BeautifulSoup(new_response.content, "html.parser")

    if url not in visited_scraped_all_links:
        news = {
            "Link": url,
            "News Category": [category.get_text(strip=True) for category in new_soup.select("span.o1byiadb.t1ktg2ut")],
            "Author": [author.get_text(strip=True) for author in new_soup.select("span.m211382")],
            "publish_time": [time.get_text(strip=True) for time in new_soup.select("span.djkus7a.m211382")],
            "Title": [title.get_text(strip=True) for title in new_soup.select("span.t1w1kov8.hhhtovw")],
            "scribe": [scribe.get_text(strip=True) for scribe in new_soup.select("p.ikh9v7p.c1bdz7f4")],
            "Text": [text.get_text(strip=True) for text in new_soup.select("div.s1am5zo.f1uhhdhr")]
        }

        visited_scraped_all_links.append(url)
        return news
    else:
        return "Scraped already"



news_links = [urljoin(start_url, link["href"]) for link in soup.select("div.i13b5qgu a")]

counter = 0
for link_to_news in news_links:
    a = extract_news(link_to_news)
    # with open("ZDF_dataset_2.json", "w", encoding="utf-8") as f:
    #     json.dump(all_news, f, ensure_ascii=False, indent=4)
    print(counter)
    counter += 1
    print(a)
    print()
    print('################' * 20)












'''
def scrape():

    if article_count > self.last_article_count:
        new_articles = article_count - self.last_article_count
        print(f"{new_articles} new articles found!")
        self.last_article_count = article_count
        all_news = []
        for link in news_links:
            news = self.extract_news(link)
            all_news.append(news)

       


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
'''