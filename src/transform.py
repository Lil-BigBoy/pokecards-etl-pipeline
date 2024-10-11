def transform_data(dataframe):

    # Check if data was successfully extracted
    if dataframe is not None:
        try:
            # Convert the DataFrame to JSON format
            json_data = dataframe.to_json(orient='records')
            return json_data
        except Exception as e:
            print(f"Error transforming data: {e}")
            return None
    else:
        print("No data to transform.")
        return None
