"""programme to craw a website for articles"""

# Tools for the project
# - requests
# - beautifulsoup

import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import csv

from .CrawledArticle import CrawledArticle

class ArticleFetcher:
    """represent a page fetcher"""

    def __init__(self) -> None:
        self.source_url = ""
        self.fetch_all_pages = False
        self.articles = []
        self.infinity_counter = 0

    def fetch(self, url, fetch_all_pages) -> None:
        """fetch articles from a page"""

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
        print("next url for fetching: " + self.source_url)
        r = requests.get(self.source_url, timeout=5)

        doc = BeautifulSoup(r.text, "html.parser")

        for card in doc.select(".card"):

            # title
            title_text = self.fetch_title_from_card(card_element = card)

            #emoji
            emoji_text = self.fetch_emoji_from_card(card_element = card)

            # content
            content_text = self.fetch_content_from_card( card_element = card )

            # image
            image_url = self.fetch_image_from_card( card_element = card )


            crawled_article = CrawledArticle(
                title_text, emoji_text, content_text, image_url
            )

            self.articles.append(crawled_article)


        # navigation to next page
        if self.fetch_all_pages:
            navigation_element = doc.select_one("div.navigation a")

            if not navigation_element:
                return

            # next page available
            navigation_element = doc.select_one("div.navigation a")
            if navigation_element is not None:
                if "href" in navigation_element.attrs:
                    next_page_url = urljoin(url, str(navigation_element.attrs["href"]))
                    self.fetch(url=next_page_url, fetch_all_pages=self.fetch_all_pages)

    def fetch_emoji_from_card(self, card_element) -> str:
        """ return the emoji url """

        emoji_text = ""
        emoji_element = card_element.select_one(".emoji")
        if emoji_element is not None:
            emoji_text = emoji_element.text
        return emoji_text

    def fetch_content_from_card(self, card_element) -> str:
        """ return the content text """

        content_text = ""
        content_element = card_element.select_one(".card-text")
        if content_element is not None:
            content_text = content_element.text

        return content_text

    def fetch_title_from_card(self, card_element) -> str:
        """ return the title text """

        title_text = ""
        title_element = card_element.select(".card-title span")[1]
        if title_element is not None:
            title_text = title_element.text

        return title_text

    def fetch_image_from_card(self, card_element) -> str:
        """ return the article image url """
        image_src = ""
        image_element = card_element.select_one("img")

        if image_element is not None:
            if "src" in image_element.attrs:
                image_src = str(image_element.attrs["src"])

        if not image_src.strip():
            return ''

        return urljoin(self.source_url, image_src)


    def receive_fetched_articles(self) -> list:
        """return the list of fetched articles"""
        return self.articles

    def export_to_csv(self, csv_file_path) -> None:
        """ save the fetched articles to a given csv file path """

        with open(csv_file_path, 'w', newline='', encoding="utf-8") as csvfile:
            column_names = ['id', 'title', 'emoji', 'content', 'image']

            # article_writer = csv.writer(csvfile, delimiter=';', quotechar='"')
            article_writer = csv.writer(csvfile, delimiter=';', quotechar='"', dialect='excel')
            article_writer.writerow(column_names)

            for article_index, article in enumerate(self.articles, 1):
                article_writer.writerow(
                    [article_index] +
                    [article.title] +
                    [article.emoji] +
                    [article.content] +
                    [article.image]
                )

            # export with DictWriter
            # column_names = ['id', 'title', 'emoji', 'content', 'image']

            # article_dict_writer = csv.DictWriter(csvfile, fieldnames=column_names, dialect='excel' )

            # article_dict_writer.writeheader()

            # for article_index, article in enumerate(self.articles, 1):
            #     article_dict_writer.writerow({
            #         'index': article_index,
            #         'title': article.title,
            #         'emoji': article.emoji,
            #         'content': article.content,
            #         'image': article.image
            #     })

        print("Article exported to: " + csv_file_path)
