import os
from src.extract import extract_dataframe  # Assuming this function extracts data from the CSV
from src.transform import transform_data  # Assuming this function transforms data to JSON

def run_generate_delivery_CSV():
    """Run the delivery generation script."""
    import src.generate_delivery_CSV

def main():
    # Step 1: Run the generate_delivery_CSV.py file
    run_generate_delivery_CSV()  # This will execute the script

    # Ensure the delivery CSV is generated before proceeding
    # Step 2: Extract data from the most recent CSV in the orders_received
    orders_received_dir = 'orders_received'
    latest_order_file = max(
        [f for f in os.listdir(orders_received_dir) if f.endswith('.csv')],
        key=lambda x: os.path.getctime(os.path.join(orders_received_dir, x))
    )
    extracted_data = extract_dataframe(os.path.join(orders_received_dir, latest_order_file))

    # Step 3: Transform dataframe to JSON format
    transformed_data = transform_data(extracted_data)

    # Step 4: Load delivery data into Pokecards database stock table
    # load_to_database(transformed_data)
    print("DATA HAS BEEN TRANSFORMED")

if __name__ == "__main__":
    main()
