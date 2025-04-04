from scraper import parser as pr
from utils import file_handler as fl
from utils import analyzer as al
if __name__ == "__main__":
    url = 'https://quotes.toscrape.com'
    parser = pr.MainParser()
    data = parser.run(url, 3)
    fileHandler = fl.SaveData()
    fileHandler.save_as_csv(data)
    fileHandler.save_as_json(data)
    print(fileHandler.load_file("data/data.csv",filetype='csv'))
    fileHandler.process_csv("data/data.csv")

    quotesData = "data/quotes_data.csv"
    authorData = "data/data_without_quotes.csv"

    fileHandler.born_date(authorData)
    fileHandler.calculate_age(authorData)

    analyze = al.Analyzer()
    analyze.frequent_tags(quotesData)
    analyze.most_frequent_authors(quotesData)
