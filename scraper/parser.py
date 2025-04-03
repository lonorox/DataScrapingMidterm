from bs4 import BeautifulSoup
import requests
from collector import Collector
from utils import analyzer as cl


class AuthorParser:

    def __init__(self):
        self.col = Collector()
        self.cleaners = cl.Cleaners()
    def get_soup(self,url):
        try:
            response = self.col.get_method(url)
            return BeautifulSoup(response.content,"html.parser")
        except  requests.exceptions.RequestException as e:
            raise e

    def get_author_info(self,url):
        soup = self.get_soup(url)
        getName = soup.select_one(".author-details > .author-title").get_text()
        getDescription = soup.select_one(".author-details > .author-description").get_text()
        getBirthDate = soup.select_one(".author-details > p >.author-born-date").get_text()
        getBirthPlace = soup.select_one(".author-details > p > .author-born-location").get_text()
        return {"name":getName,"birthDate" : getBirthDate, "birthPlace" : getBirthPlace, "description":getDescription}


