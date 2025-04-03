from http.client import responses

from bs4 import BeautifulSoup
import requests
from collector import Collector
from DataScrapingMidterm.utils import prettier as pr
from DataScrapingMidterm.models import data_models as dm
from datetime import datetime


class AuthorParser:

    def get_soup(self, url):
        response = Collector.get_method(url)
        return BeautifulSoup(response.text, "html.parser")

    def get_author_info(self, url):
        soup = self.get_soup(url)
        getName = soup.select_one(".author-details > .author-title").get_text()
        getName = pr.cleaner(getName)
        getDescription = soup.select_one(".author-details > .author-description").get_text()
        getDescription = pr.cleaner(getDescription)
        getBirthDate = soup.select_one(".author-details > p >.author-born-date").get_text()
        getBirthPlace = soup.select_one(".author-details > p > .author-born-location").get_text()
        getBirthPlace = pr.cleaner(getBirthPlace)
        getBirthDate = datetime.strptime(getBirthDate, "%B %d, %Y")
        authorData = dm.Author(getName, getBirthDate, getBirthPlace, getDescription, [])
        return authorData

test_url = 'https://quotes.toscrape.com/author/Albert-Einstein/'

a = AuthorParser()
print(a.get_author_info(test_url).to_dict())


#
# def main_parser():
#     website = 'https://quotes.toscrape.com'
#     current_page = '/page/1/'
#     ##
#     data = {}
#     a = AuthorParser()
#     responses = a.col.get_method()
