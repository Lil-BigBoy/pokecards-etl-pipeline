import pandas as pd

def extract_data(csv_file: str):
    try:
        data = pd.read_csv(csv_file)
        return data
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None
