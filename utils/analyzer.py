import os

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from DataScrapingMidterm.utils import file_handler as fl


class Analyzer:
    def frequent_tags(self, file):
        df_quotes = fl.SaveData().load_file(file, "csv")
        # Flatten all tags into a single untransformedJsonAuthorQuoteList
        all_tags = []
        if 'tags' not in df_quotes.columns:
            raise KeyError("The 'tags' column is missing in the quotes data.")

        for tags in df_quotes['tags']:
            # Ensure that each entry in the 'tags' column is a string or an empty value
            # Split and add to the all_tags untransformedJsonAuthorQuoteList,
            # handling cases where tags might be empty or malformed
            if tags:  # Ensure the tag is not empty
                all_tags.extend(str(tags).split(", "))  # Split and add to the untransformedJsonAuthorQuoteList
            else:
                print("Empty tags encountered; skipping.")

        # Count frequency of each tag
        tag_counts = pd.Series(all_tags).value_counts()
        topTenTags = tag_counts.head(10)  # Top 10 most frequent tags

        # Plot the top 10 most frequent tags
        plt.figure(figsize=(10, 6))
        topTenTags.plot(kind='bar', color='skyblue')
        plt.title('Top 10 Most Frequent Tags in Quotes')
        plt.xlabel('Tags')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        os.makedirs("data/analyzedImages", exist_ok=True)
        plot_filename = "data/analyzedImages/most_frequent_tags.png"
        plt.savefig(plot_filename, bbox_inches='tight')  # Saves and overwrites if it exists
        plt.show()
        plt.close()

    def most_frequent_authors(self, file):
        df = fl.SaveData().load_file(file, "csv")
        author_counts = df['name'].value_counts()
        # Show the top 5 most frequent authors

        plt.figure(figsize=(10, 6))
        author_counts.head(10).plot(kind='bar', color='skyblue')
        plt.title('Top 10 Most Frequent Authors in Quotes')
        plt.xlabel('authors')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        os.makedirs("data/analyzedImages", exist_ok=True)
        plot_filename = "data/analyzedImages/most_frequent_authors.png"
        plt.savefig(plot_filename, bbox_inches='tight')  # Saves and overwrites if it exists
        plt.show()
        plt.close()
