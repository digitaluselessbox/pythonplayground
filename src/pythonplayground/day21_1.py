""" crawling a website """

import crawler

fetcher = crawler.ArticleFetcher()

fetcher.fetch(
	url="https://python.beispiel.programmierenlernen.io/index.php",
    fetch_all_pages=False
)

fetched_articles = fetcher.receive_fetched_articles()
print(f"There were {len(fetched_articles)} articles fetched.")
