from bs4 import BeautifulSoup
from wheel.cli import tags_f

from DataScrapingMidterm.scraper.collector import Collector
from DataScrapingMidterm.utils import text_transformers as pr
from DataScrapingMidterm.models import data_models as dm
from datetime import datetime


class AuthorParser:

    def get_soup(self, url):
        response = Collector.get_method(url)
        return BeautifulSoup(response.text, 'html.parser')

    def get_author(self, url):
        soup = self.get_soup(url)
        getName = soup.select_one(".author-details > .author-title").get_text()
        getName = pr.cleaner(getName)

        getDescription = soup.select_one(".author-details > .author-description").get_text()[:50]
        getDescription = pr.cleaner(getDescription)

        getBirthDate = soup.select_one(".author-details > p >.author-born-date").get_text()

        getBirthPlace = soup.select_one(".author-details > p > .author-born-location").get_text()

        getBirthPlace = pr.cleaner(getBirthPlace)
        getBirthDate = datetime.strptime(getBirthDate, "%B %d, %Y").isoformat()

        return dm.Author(getName, getBirthDate, getBirthPlace, getDescription, [])


class QuoteParser:
    def get_link(self, soup: BeautifulSoup):
        return soup.select_one('a').get('href')

    def get_quote(self, soup: BeautifulSoup):
        text = soup.select_one('span.text').text
        tags = [i.text for i in soup.select('div.tags a')]
        return dm.Quote(text, tags)


class MainParser:
    def __init__(self):
        self.list = []
    def next_page(self,url):
        response = Collector.get_method(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        nextURL =soup.find('li',class_='next').find('a').get('href')
        return nextURL
    def run(self, url, pages=1):
        current_page = '/page/1/'
        counter = 0
        author_set = set()
        data = {}
        while True:
            response = Collector.get_method(f'{url}{current_page}')
            if not response or counter >= pages:
                break

            soup = BeautifulSoup(response.text, 'html.parser')

            quoteParser = QuoteParser()
            authorParser = AuthorParser()

            for b in soup.select('div.quote'):

                quote = quoteParser.get_quote(b)
                author_link = f'{url}{quoteParser.get_link(b)}'
                Author = authorParser.get_author(author_link)

                if Author.name not in author_set:

                    author_set.add(Author.name)
                    Author.append_quotes(quote)
                    data[Author.name] = Author

                else:
                    data[Author.name].append_quotes(quote)

            current_page =  self.next_page(f'{url}{current_page}')
            counter += 1

        for v in data.values():
            self.list.append(v.to_dict())
        return self.list