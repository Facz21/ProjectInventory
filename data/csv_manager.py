# IMPORTS 
import csv

# Path to the CSV file where data is stored
DB_PATH = "db/data.csv"


# LOAD DATA 

def load_data():
    """
    Loads product data from the CSV file.

    Converts each row into a dictionary and ensures:
    - id → int
    - quantity → int
    - price → float

    Returns:
        list: List of product dictionaries
    """

    products = []

    try:
        with open(DB_PATH, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "quantity": int(row["quantity"]),
                    "price": float(row["price"])
                })

    except FileNotFoundError:
        # If the file does not exist, return an empty list
        return []

    return products


# SAVE DATA 

def save_data(products):
    """
    Saves product data into the CSV file.

    Overwrites the file and writes:
    - Header row
    - All product data

    Args:
        products (list): List of product dictionaries
    """

    with open(DB_PATH, mode="w", newline="") as file:
        fieldnames = ["id", "name", "quantity", "price"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write column headers
        writer.writeheader()

        # Write all product rows
        writer.writerows(products)