import pandas as pd
import random
import os

# Complete list of Base Set card information
base_set_cards = [
    {"name": "Alakazam", "type": "Psychic", "rarity": "Rare"},
    {"name": "Blastoise", "type": "Water", "rarity": "Rare"},
    {"name": "Chansey", "type": "Colorless", "rarity": "Rare"},
    {"name": "Charizard", "type": "Fire", "rarity": "Rare"},
    {"name": "Clefairy", "type": "Colorless", "rarity": "Common"},
    {"name": "Gyarados", "type": "Water", "rarity": "Rare"},
    {"name": "Hitmonchan", "type": "Fighting", "rarity": "Rare"},
    {"name": "Machamp", "type": "Fighting", "rarity": "Rare"},
    {"name": "Magneton", "type": "Electric", "rarity": "Rare"},
    {"name": "Mewtwo", "type": "Psychic", "rarity": "Rare"},
    {"name": "Nidoking", "type": "Poison", "rarity": "Rare"},
    {"name": "Ninetales", "type": "Fire", "rarity": "Rare"},
    {"name": "Poliwrath", "type": "Water", "rarity": "Rare"},
    {"name": "Raichu", "type": "Electric", "rarity": "Rare"},
    {"name": "Venusaur", "type": "Grass", "rarity": "Rare"},
    {"name": "Zapdos", "type": "Electric", "rarity": "Rare"},
    {"name": "Beedrill", "type": "Grass", "rarity": "Rare"},
    {"name": "Dragonair", "type": "Dragon", "rarity": "Uncommon"},
    {"name": "Dugtrio", "type": "Ground", "rarity": "Uncommon"},
    {"name": "Electabuzz", "type": "Electric", "rarity": "Common"},
    {"name": "Electrode", "type": "Electric", "rarity": "Uncommon"},
    {"name": "Pidgeotto", "type": "Colorless", "rarity": "Uncommon"},
    {"name": "Arcanine", "type": "Fire", "rarity": "Uncommon"},
    {"name": "Charmeleon", "type": "Fire", "rarity": "Uncommon"},
    {"name": "Dewgong", "type": "Water", "rarity": "Uncommon"},
    {"name": "Dratini", "type": "Dragon", "rarity": "Common"},
    {"name": "Farfetch'd", "type": "Colorless", "rarity": "Uncommon"},
    {"name": "Growlithe", "type": "Fire", "rarity": "Common"},
    {"name": "Haunter", "type": "Ghost", "rarity": "Uncommon"},
    {"name": "Ivysaur", "type": "Grass", "rarity": "Uncommon"},
    {"name": "Jynx", "type": "Ice", "rarity": "Uncommon"},
    {"name": "Kadabra", "type": "Psychic", "rarity": "Uncommon"},
    {"name": "Kakuna", "type": "Grass", "rarity": "Common"},
    {"name": "Machoke", "type": "Fighting", "rarity": "Uncommon"},
    {"name": "Magikarp", "type": "Water", "rarity": "Common"},
    {"name": "Magmar", "type": "Fire", "rarity": "Common"},
    {"name": "Nidorino", "type": "Poison", "rarity": "Uncommon"},
    {"name": "Poliwhirl", "type": "Water", "rarity": "Uncommon"},
    {"name": "Porygon", "type": "Colorless", "rarity": "Common"},
    {"name": "Raticate", "type": "Colorless", "rarity": "Common"},
    {"name": "Seel", "type": "Water", "rarity": "Common"},
    {"name": "Wartortle", "type": "Water", "rarity": "Uncommon"},
    {"name": "Abra", "type": "Psychic", "rarity": "Common"},
    {"name": "Bulbasaur", "type": "Grass", "rarity": "Common"},
    {"name": "Caterpie", "type": "Grass", "rarity": "Common"},
    {"name": "Charmander", "type": "Fire", "rarity": "Common"},
    {"name": "Diglett", "type": "Ground", "rarity": "Common"},
    {"name": "Doduo", "type": "Colorless", "rarity": "Common"},
    {"name": "Drowzee", "type": "Psychic", "rarity": "Common"},
    {"name": "Gastly", "type": "Ghost", "rarity": "Common"},
    {"name": "Koffing", "type": "Poison", "rarity": "Common"},
    {"name": "Machop", "type": "Fighting", "rarity": "Common"},
    {"name": "Magnemite", "type": "Electric", "rarity": "Common"},
    {"name": "Metapod", "type": "Grass", "rarity": "Common"},
    {"name": "Nidoran", "type": "Poison", "rarity": "Common"},
    {"name": "Onix", "type": "Rock", "rarity": "Common"},
    {"name": "Pidgey", "type": "Colorless", "rarity": "Common"},
    {"name": "Pikachu", "type": "Electric", "rarity": "Common"},
    {"name": "Poliwag", "type": "Water", "rarity": "Common"},
    {"name": "Ponyta", "type": "Fire", "rarity": "Common"},
    {"name": "Rattata", "type": "Colorless", "rarity": "Common"},
    {"name": "Sandshrew", "type": "Ground", "rarity": "Common"},
    {"name": "Squirtle", "type": "Water", "rarity": "Common"},
    {"name": "Starmie", "type": "Water", "rarity": "Uncommon"},
    {"name": "Staryu", "type": "Water", "rarity": "Common"},
    {"name": "Tangela", "type": "Grass", "rarity": "Common"},
    {"name": "Voltorb", "type": "Electric", "rarity": "Common"},
    {"name": "Vulpix", "type": "Fire", "rarity": "Common"},
    {"name": "Weedle", "type": "Grass", "rarity": "Common"},
    {"name": "Clefairy Doll", "type": "Trainer", "rarity": "Common"},
    {"name": "Computer Search", "type": "Trainer", "rarity": "Rare"},
    {"name": "Devolution Spray", "type": "Trainer", "rarity": "Uncommon"},
    {"name": "Imposter Professor Oak", "type": "Trainer", "rarity": "Uncommon"},
    {"name": "Item Finder", "type": "Trainer", "rarity": "Uncommon"},
    {"name": "Lass", "type": "Trainer", "rarity": "Uncommon"},
    {"name": "Pokemon Breeder", "type": "Trainer", "rarity": "Rare"},
    {"name": "Pokemon Trader", "type": "Trainer", "rarity": "Uncommon"},
    {"name": "Scoop Up", "type": "Trainer", "rarity": "Uncommon"},
    {"name": "Super Energy Removal", "type": "Trainer", "rarity": "Uncommon"},
    {"name": "Defender", "type": "Trainer", "rarity": "Common"},
    {"name": "Energy Retrieval", "type": "Trainer", "rarity": "Common"},
    {"name": "Full Heal", "type": "Trainer", "rarity": "Common"},
    {"name": "Maintenance", "type": "Trainer", "rarity": "Common"},
    {"name": "PlusPower", "type": "Trainer", "rarity": "Common"},
    {"name": "Pokemon Center", "type": "Trainer", "rarity": "Rare"},
    {"name": "Pokemon Flute", "type": "Trainer", "rarity": "Uncommon"},
    {"name": "Pokedex", "type": "Trainer", "rarity": "Common"},
    {"name": "Professor Oak", "type": "Trainer", "rarity": "Rare"},
    {"name": "Revive", "type": "Trainer", "rarity": "Common"},
    {"name": "Super Potion", "type": "Trainer", "rarity": "Uncommon"},
    {"name": "Bill", "type": "Trainer", "rarity": "Common"},
    {"name": "Energy Removal", "type": "Trainer", "rarity": "Common"},
    {"name": "Gust of Wind", "type": "Trainer", "rarity": "Common"},
    {"name": "Potion", "type": "Trainer", "rarity": "Common"},
    {"name": "Switch", "type": "Trainer", "rarity": "Common"},
    {"name": "Double Colorless Energy", "type": "Energy", "rarity": "Rare"},
    {"name": "Fighting Energy", "type": "Energy", "rarity": "Common"},
    {"name": "Fire Energy", "type": "Energy", "rarity": "Common"},
    {"name": "Grass Energy", "type": "Energy", "rarity": "Common"},
    {"name": "Lightning Energy", "type": "Energy", "rarity": "Common"},
    {"name": "Psychic Energy", "type": "Energy", "rarity": "Common"},
    {"name": "Water Energy", "type": "Energy", "rarity": "Common"}
]

# Total count
assert len(base_set_cards) == 102, "Total number of cards should be 102"

# Function to generate price based on rarity
def get_price(rarity):
    if rarity == "Common":
        return round(random.uniform(0.50, 1.50), 2)
    elif rarity == "Uncommon":
        return round(random.uniform(1.50, 4.50), 2)
    elif rarity == "Rare":
        return round(random.uniform(5.00, 100.00), 2)

# Create DataFrame
def generate_weekly_delivery():
    data = []
    pricelist_path = os.path.join('supplier_pricing', 'price_list.csv')
    
    # Load the price list into a DataFrame
    if os.path.exists(pricelist_path):
        pricelist_df = pd.read_csv(pricelist_path)
    else:
        pricelist_df = pd.DataFrame(columns=['Card', 'Product ID', 'Cost'])
    for idx, card in enumerate(base_set_cards, start=1):
        

        matching_card = pricelist_df[pricelist_df['Card'] == card['name']]
        
        if not matching_card.empty:
            # Use the existing price from pricelist
            price = matching_card['Cost'].values[0]
        else:
            # Generate new price if card is not found
            price = get_price(card['rarity'])
            # Append the new card and price to the pricelist DataFrame
            new_entry = pd.DataFrame({
                'Product ID': [f"{idx:03}"], 
                'Card': [card['name']],
                'Set': 'Base Set', # CHANGE HOW THIS IS IMPLEMENTED
                'Cost': [price]
            })
            pricelist_df = pd.concat([pricelist_df, new_entry], ignore_index=True)
            # Save the updated pricelist to CSV
            pricelist_df.to_csv(pricelist_path, index=False)


        orderQuantity = random.randint(10, 30) if card["rarity"] == "Common" else random.randint(30, 50) if card["rarity"] == "Uncommon" else random.randint(10, 30)

        total_cost = round(price * orderQuantity, 2)
        data.append({
            "Product ID": f"CC{idx + 516:04}",
            "Card": card["name"],
            "Card Type": card["type"],
            "Card Set": "Base Set", # CHANGE HOW THIS IS IMPLEMENTED WITH ADDITIONAL CARD SETS (e.g. make outer loop for sets where set name is ripped from the global variable name and altered accordingly)
            "Rarity": card["rarity"],
            "Cost": price,
            "Quantity": orderQuantity,
            "Total Cost": total_cost
        })
    return pd.DataFrame(data)

# Directory for orders
orders_received = 'orders_received'

# Count the number of existing weekly orders in the 'orders_received' folder
def get_week_number(orders_received):
    # Ensure the folder exists
    if not os.path.exists(orders_received):
        os.makedirs(orders_received)
        return 1  # If folder is empty or newly created, start with week 1

    # Get list of all CSV files in the folder
    files = [file for file in os.listdir(orders_received) if file.endswith('.csv')]

    # Week number is the count of CSV files + 1
    return len(files) + 1

# Generate and save weekly order
def save_weekly_delivery(df, orders_received):
    week_number = get_week_number(orders_received)

    # Simulate date based on week_number (just for illustrative purposes)
    # For example, start from a fixed date like 1st Feb 2025
    start_date = pd.to_datetime('2025-02-08')
    week_date = start_date + pd.DateOffset(weeks=week_number-1)

    # Format the date to ddmmyy for the filename
    formatted_date = week_date.strftime('%d%m%y')

    # Set the DataFrame name as a CSV file with the week date
    filename = f'weekly_order_{formatted_date}.csv'
    file_path = os.path.join(orders_received, filename)

    # Save the DataFrame as CSV
    df.to_csv(file_path, index=False)
    print(f"Weekly order saved as {file_path}")

# Generate weekly order data
weekly_order_df = generate_weekly_delivery()

# Save the order
save_weekly_delivery(weekly_order_df, orders_received)
