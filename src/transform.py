from src.extract import extract_data

def transform_data(dataframe):
    try:
        # Use the existing function to extract data
        data = extract_data(dataframe)

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
    