import json
import pandas as pd
import os
import ast
from datetime import datetime
class SaveData:
    def save_as_json(self, data):
        try:
            os.makedirs("data", exist_ok=True)  # Ensure the directory exists
            with open("data/data.json", "w") as file:
                json.dump(data, file, indent=4)
        except (OSError, IOError) as e:
            print(f"Error saving JSON file: {e}")
        except TypeError as e:
            print(f"Invalid data type for JSON: {e}")

    def save_as_csv(self, data):
        try:
            if not isinstance(data, list):
                raise ValueError("Data should be a list of dictionaries or lists.")
            os.makedirs("data", exist_ok=True)  # Ensure the directory exists
            df = pd.DataFrame(data)
            df.to_csv("data/data.csv", index=False, mode='w')
        except ValueError as e:
            print(f"Invalid data format: {e}")
        except (OSError, IOError) as e:
            print(f"Error saving CSV file: {e}")
    """method load_file loads either or csv or json file. process_csv transforms csv data"""
    def load_file(self, file, filetype="json"):
        try:
            if filetype == "json":
                if not os.path.exists(file):
                    raise FileNotFoundError(f"JSON file not found in '{file}'")
                with open(file, "r") as file:
                    data = json.load(file)
                print(f"Loaded JSON data from '{file}'.")

            elif filetype == "csv":
                if not os.path.exists(file):
                    raise FileNotFoundError(f"CSV file not found in '{file}'")
                # data = pd.read_csv(path).to_dict(orient="records")
                data = pd.read_csv(file)
                print(f"Loaded CSV data from '{file}'.")

            else:
                raise ValueError("Invalid filetype. Use 'json' or 'csv'.")

            return data

        except Exception as e:
            print(f"Error loading or processing data: {e}")
            return None

    def process_csv(self, file):
        try:
            df = self.load_file(file, "csv")
            # Ensure 'quotes' column exists
            if 'quotes' not in df.columns:
                raise KeyError("The 'quotes' column is missing in the CSV file.")
            # Parse the quotes column as a list of dictionaries
            df['quotes'] = df['quotes'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
            # Split data into two dataframes
            # Everything without the 'quotes' column
            df_without_quotes = df.drop(columns=["quotes"])
            # Only name, quote, and tags
            quotes_data = []
            for _, row in df.iterrows():
                name = row['name']
                if isinstance(row['quotes'], list):
                    for quote_entry in row['quotes']:
                        # Ensure 'text' and 'tags' keys exist in each quote entry
                        if not isinstance(quote_entry, dict):
                            raise ValueError(
                                f"Invalid quote format for name {name}. Expected a dictionary, but got {type(quote_entry)}.")
                        quotes_data.append({
                            "name": name,
                            "quote": quote_entry.get("text", ""),
                            "tags": ", ".join(quote_entry.get("tags", []))  # Join tags as a string
                        })

            # Create DataFrame for quotes
            df_quotes = pd.DataFrame(quotes_data)
            # Ensure the 'data' directory exists
            os.makedirs("data", exist_ok=True)
            # Save to CSVs
            df_without_quotes.to_csv("data/data_without_quotes.csv", index=False)
            df_quotes.to_csv("data/quotes_data.csv", index=False)
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except pd.errors.EmptyDataError:
            print(f"{file} is empty.")
        except pd.errors.ParserError:
            print(f"Error: The file '{file}' could not be parsed.")
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
        except (OSError, IOError) as e:
            print(f"Error saving files: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def born_date(self,file):
        df = self.load_file(file, "csv")
        # Convert 'born_date' to datetime and then to a more human-readable format
        df['born_date'] = pd.to_datetime(df['born_date']).dt.strftime('%B %d, %Y')

        # Save the transformed data back to CSV
        df.to_csv("final_data.csv", index=False)

    def calculate_age(self,file):
        df = self.load_file(file, "csv")
        current_date = datetime.now()
        df['born_date'] = pd.to_datetime(df['born_date'])

        # Calculate age at the current date and add a new 'age_at_current_date' column
        df['age_at_current_date'] = df['born_date'].apply(
            lambda x: current_date.year - x.year - ((current_date.month, current_date.day) < (x.month, x.day)))

        # Save the transformed data with age back to CSV (optional)
        df.to_csv("data/transformed_data_with_age.csv", index=False)