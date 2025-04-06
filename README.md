# DataScrapingMidterm
This project scrapes author and quote data from https://quotes.toscrape.com.

**How to Run**:

	1.	Open main.py.
	2.	To start the scraper, run the main() function.
	3.	To adjust the number of pages to scrape, change the value of:
        pages_to_Scrap = 5

**Data Folder Structure**

data/raw/ -
Contains the initially parsed data:

	•	data.csv: Includes all authors with the following information:
	•	Name
	•	Birthplace
	•	Birthdate
	•	Short description
	•	List of quotes (each with associated tags)
	•	data.json: Same content in JSON format.

data/transformed/ -
Contains cleaned and structured CSV files:

	•	authors_before.csv: Author details only (no quotes).
	•	quotes.csv: Flattened list of quotes, including author names and tags.
	•	authors_after.csv: Same as authors_before.csv, but birthdates are converted to a human-readable format (e.g., "April 6, 2025").
	•	authors_with_current_ages.csv: Adds a column calculating the author’s age based on the current date.

data/analyzedImages/ -
Contains visualizations:

	•	most_frequent_authors.png: Bar chart of the most frequently quoted authors.
	•	most_frequent_tags.png: Bar chart of the most commonly used tags.


**Code Overview**

scraper/collector.py - is a python file that handles http requests
scraper/parser.py - is responsible for parsing a website.

    Class: AuthorParser -Parses information about authors from individual author pages.
    
	    •get_author(url) - Extracts and returns an Author object by scraping name, birthdate, birthplace, and a short 
            description from the author’s page.

    Class: QuoteParser - Parses quotes and author links from quote blocks on a page.
	    •get_link(soup) - Extracts the relative URL to the author’s page from a quote block.
	    •get_quote(soup) - Extracts the quote text and associated tags, returning a Quote object.

    Class: MainParser - Controls the main scraping loop and combines author and quote data.
	    •next_page(url) - Parses the next page link from the pagination section to continue scraping.
	    •run(url, pages=1) - Main execution method. Iterates through pages, extracts quotes and author info, avoids 
            duplicates, and returns a list of author data with associated quotes.

utils/file_handler.py - is responsible for saving data into file and transforming them

    Class: SaveData - Handles saving, loading, transforming, and analyzing scraped author and quote data.
    
        •save_as_json(data) - Saves the given data to a JSON file at data/raw/data.json. Creates the directory if it 
            doesn’t exist.
        •save_as_csv(data) - Saves the given data (expected to be a list of dictionaries) to a CSV file at 
            data/raw/data.csv. Creates the directory if needed.

        •load_file(file, filetype="json") - Loads and returns data from a .json or .csv file. For JSON Returns parsed 
            Python objects, for CSV it  Returns a Pandas DataFrame.

        •process_csv(file) - Transforms a CSV file that includes an embedded quotes column (as a stringified list of 
            dictionaries). Splits data into:
                •	authors_before.csv: Author data without quotes.
                •	quotes.csv: Flattened quote data with tags and author names.
                •	Saves output in data/transformed/.

        •born_date(file) - Converts the born_date column in a CSV to a human-readable format (e.g., "April 6, 2025") 
            and saves the result as authors_after.csv.

        •calculate_age(file) - Calculates the current age of each author based on their birthdate and adds a new column 
            age_at_current_date. Saves to authors_with_current_ages.csv.

utils/analyzer.py - is responsible for analyzing collected data.

     Class: Analyzer - Analyzes author and quote data from CSV files and visualizes insights with bar charts.

    frequent_tags(file)
	•	Loads a CSV file containing quotes.
	•	Extracts and counts the most frequent tags used in quotes.
	•	Plots and saves a bar chart of the top 10 most frequent tags in data/analyzedImages/most_frequent_tags.png.

    most_frequent_authors(file)
        •	Loads a CSV file containing quotes.
        •	Counts how many quotes are attributed to each author.
        •	Plots and saves a bar chart of the top 10 most quoted authors in data/analyzedImages/most_frequent_authors.png.
