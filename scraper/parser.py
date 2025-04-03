from bs4 import BeautifulSoup
import requests
from collector import Collector
from utils import analyzer as cl
from models import data_models as dm
from datetime import datetime
class AuthorParser:

    def __init__(self):
        self.col = Collector()
        self.cleaners = cl.Cleaners
        # self.data =
    def get_soup(self,url):
        try:
            response = self.col.get_method(url)
            return BeautifulSoup(response.content,"html.parser")
        except  requests.exceptions.RequestException as e:
            raise e

    def get_author_info(self,url):
        soup = self.get_soup(url)
        getName = soup.select_one(".author-details > .author-title").get_text()
        getName = self.cleaners.cleaner(getName)
        getDescription = soup.select_one(".author-details > .author-description").get_text()
        getDescription = self.cleaners.cleaner(getDescription)
        getBirthDate = soup.select_one(".author-details > p >.author-born-date").get_text()
        getBirthPlace = soup.select_one(".author-details > p > .author-born-location").get_text()
        getBirthPlace = self.cleaners.cleaner(getBirthPlace)
        getBirthDate = datetime.strptime(getBirthDate, "%B %d, %Y")
        authorData = dm.Author(getName,getBirthDate,getBirthPlace,getDescription,[])
        return authorData


if __name__ == "__main__":
    a = AuthorParser()
    data = a.get_author_info("http://quotes.toscrape.com/author/Eleanor-Roosevelt/")
    print(data)