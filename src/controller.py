import os
import time

from extract import extract_dataframe
from transform import transform_data
from load import update_database

def generate_delivery():
    """Run the delivery generation script by importing it."""
    import generate_delivery_CSV

def delivery_day():
    # Count files in the orders_received directory
    order_count = len(os.listdir('orders_received'))

    # Run the generate_delivery_CSV.py file
    generate_delivery()

    # Ensure the delivery CSV is generated before proceeding
    while True:
        current_count = len(os.listdir('orders_received'))
        if current_count > order_count:  # Check if the count has increased
            print("New delivery file detected.")
            break  # Exit the loop if a new file is detected
        else:
            print("Waiting for new delivery file...")
            time.sleep(1)  # Wait for 1 second before checking again

    # Extract data from the most recent CSV in the orders_received
    orders_dir = 'orders_received'
    latest_order = max(
        [f for f in os.listdir(orders_dir) if f.endswith('.csv')],
        key=lambda x: os.path.getctime(os.path.join(orders_dir, x))
    )
    extracted_data = extract_dataframe(os.path.join(orders_dir, latest_order))

    # Step 3: Transform dataframe to JSON format
    transformed_data = transform_data(extracted_data)

    # Step 4: Load delivery data into Pokecards database stock table
    update_database(transformed_data)

if __name__ == "__main__":
    delivery_day()
