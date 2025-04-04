from scraper import parser as pr
from utils import file_handler as fl
from utils import analyzer as al

if __name__ == "__main__":

    # scrapping first 5 pages of quotes.toscrape.com website
    url = 'https://quotes.toscrape.com'
    pages_to_Scrap = 5

    #  Initializing Handler class objects
    parser = pr.MainParser()
    fileHandler = fl.SaveData()
    analyzer = al.Analyzer()
    # parsing data and returning j
    untransformedJsonAuthorQuoteList = parser.run(url, pages_to_Scrap)

    # saving  untransformedJsonAuthorQuoteList into csv and json formats in data directory  as data.csv and data.json
    fileHandler.save_as_csv(untransformedJsonAuthorQuoteList)
    fileHandler.save_as_json(untransformedJsonAuthorQuoteList)

    # showing raw untransformedJsonAuthorQuoteList
    print(fileHandler.load_file("data/raw/data.csv", filetype='csv'))
    print(fileHandler.load_file("data/raw/data.json", filetype='json'))

    # processing raw  untransformedJsonAuthorQuoteList
    fileHandler.process_csv("data/raw/data.csv")

    # specifying files paths that are created after process_csv()
    quotesData = "data/transformed/quotes.csv"
    authorData = "data/transformed/authors_before.csv"

    # creating and adding transformed files to data/transformed folder
    fileHandler.born_date(authorData)
    fileHandler.calculate_age(authorData)
    # creating and adding and plotting analyzed images to data/analyzedImages folder
    analyzer.frequent_tags(quotesData)
    analyzer.most_frequent_authors(quotesData)
