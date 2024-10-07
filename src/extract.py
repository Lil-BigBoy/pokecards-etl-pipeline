import pandas as pd

def extract_dataframe(csv_file):
    try:
        dataframe = pd.read_csv(csv_file)
        return dataframe
    except Exception as e:
        print(f"Error extracting dataframe: {e}")
        return None
