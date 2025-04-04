import json
import pandas as pd
import os
import ast
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

