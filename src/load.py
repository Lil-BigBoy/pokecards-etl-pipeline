import psycopg2
import json

def connect_to_db():
    # Replace with your connection details
    conn = psycopg2.connect("dbname='pokecards_db' user='rob' password='PSQLCollege1!' host='localhost'")
    return conn

def update_database(JSON):

    cards = json.loads(JSON)

    conn = connect_to_db()
    cursor = conn.cursor()

    for card in cards:
        # Check if the card exists by both name and set
        cursor.execute("SELECT * FROM stock WHERE name_of_card = %s AND card_set = %s", (card['Card'], card['Card Set']))
        existing_card = cursor.fetchone()
        
        if existing_card:
            # Update the existing card's stock
            new_stock = existing_card[6] + card['Quantity']
            cursor.execute("UPDATE stock SET quantity = %s WHERE name_of_card = %s AND card_set = %s",
                           (new_stock, card['Card'], card['Card Set']))
        else:
            # Insert new card with 60% markup on sales
            sale_price = card['Cost'] * 1.6
            # Use supplier product ID to formatt our stock numbers
            stock_number = f"{int(card['Product ID'][2:]) - 516:03}"

            cursor.execute("INSERT INTO stock (stock_number, name_of_card, type_of_card, card_set, rarity, sale_price, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (stock_number, card['Card'], card['Card Type'], card['Card Set'], card['Rarity'], sale_price, card['Quantity']))

    conn.commit()
    cursor.close()
    conn.close()
