import psycopg2
from src.transform import transform_data

def connect_to_db():
    # Replace with your connection details
    conn = psycopg2.connect("dbname='yourdbname' user='youruser' password='yourpassword' host='localhost'")
    return conn

def update_database(dataframe):
    conn = connect_to_db()
    cursor = conn.cursor()

    for index, row in dataframe.iterrows():
        # Check if the card exists by both name and set
        cursor.execute("SELECT * FROM pokecards WHERE name = %s AND card_set = %s", (row['name'], row['card_set']))
        existing_card = cursor.fetchone()
        
        if existing_card:
            # Update the existing card's stock
            new_stock = existing_card[6] + row['stock']  # Adjust index as necessary
            cursor.execute("UPDATE pokecards SET stock = %s WHERE name = %s AND card_set = %s", 
                           (new_stock, row['name'], row['card_set']))
        else:
            # Insert new card
            cursor.execute("INSERT INTO pokecards (unique_stock_number, name, type, card_set, rarity, sale_price, stock) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (row['unique_stock_number'], row['name'], row['type'], row['card_set'], row['rarity'], row['sale_price'], row['stock']))

    conn.commit()
    cursor.close()
    conn.close()
