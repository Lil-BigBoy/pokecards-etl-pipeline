import psycopg2

def connect_to_db():
    # Replace with your connection details
    conn = psycopg2.connect("dbname='pokecards_db' user='rob' password='PSQLCollege1!' host='localhost'")
    return conn

def update_database(JSON):
    conn = connect_to_db()
    cursor = conn.cursor()

    for card in JSON.iterrows():
        # Check if the card exists by both name and set
        cursor.execute("SELECT * FROM stock WHERE name = %s AND card_set = %s", (row['name'], card['card_set']))
        existing_card = cursor.fetchone()
        
        if existing_card:
            # Update the existing card's stock
            new_stock = existing_card[6] + card['quantity']  # Adjust index as necessary
            cursor.execute("UPDATE stock SET quantity = %s WHERE name = %s AND card_set = %s",
                           (new_stock, card['name'], card['card_set']))
        else:
            # Insert new card
            cursor.execute("INSERT INTO stock (name, type, card_set, rarity, sale_price, stock) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (card['name'], card['type'], card['card_set'], card['rarity'], card['sale_price'], card['stock']))

    conn.commit()
    cursor.close()
    conn.close()
