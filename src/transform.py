import pandas as pd
from etl import extract_data  # Import the extract_data function

def transform_data(csv_file):
    try:
        # Use the existing function to extract data
        data = extract_data(csv_file)

        # Check if data was successfully extracted
        if data is not None:
            # Convert the DataFrame to JSON format
            json_data = data.to_json(orient='records', lines=True)
            return json_data
        else:
            print("No data to transform.")
            return None
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None
    