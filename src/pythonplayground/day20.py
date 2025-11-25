""" programme to craw a website for articles """

# Tools for the project
# - requests
# - beautifulsoup

import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class CrawlArticle:
    """ represent a fetched article """
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image


class ArticleFetcher:
    """ represent a page fetcher """

    def __init__(self) -> None:
        self.source_url = ''
        self.fetch_all_pages = False
        self.articles = []
        self.infinity_counter = 0


    def fetch(self, url, fetch_all_pages) -> None:
        """ fetch articles from a page """

        self.source_url = url
        self.fetch_all_pages = fetch_all_pages

        # just for safety. Maybe later it become a page amount fetch limit
        self.infinity_counter += 1
        if self.infinity_counter > 10:
            print("WHOA!!! To many fetch request.")
            print("Possible reachout to infinity.")
            print("DO NOT GO INTO THE LIGHT!!")
            exit()


        # more safety an restrained
        time.sleep(1)
        print(url)
        r = requests.get(url, timeout=5)
        doc = BeautifulSoup(r.text, "html.parser")

        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title = card.select(".card-title span")[1].text
            image = urljoin(url, card.select_one("img").attrs["src"])

            crawled_article = CrawlArticle(title, emoji, content, image)

            self.articles.append(crawled_article)

        # navigation to next page
        if self.fetch_all_pages:
            navigation_element = doc.select_one("div.navigation a")

            if not navigation_element:
                return


            # next page available
            next_page_url = urljoin(url, doc.select_one("div.navigation a").attrs["href"] )
            self.fetch(url = next_page_url, fetch_all_pages = self.fetch_all_pages)


    def receive_fetched_articles(self) -> list:
        """ return the list of fetched articles """
        return self.articles



fetcher = ArticleFetcher()
fetcher.fetch(
    url="https://python.beispiel.programmierenlernen.io/index.php",
    fetch_all_pages = True
)

fetched_articles = fetcher.receive_fetched_articles()

print(f"There were {len(fetched_articles)} articles fetched.")
for article_index, article in enumerate(fetched_articles, 1):
    print(f"--- Article Number: {article_index} ------------------")
    print(article.title)
    print(article.image)
