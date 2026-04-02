import csv

DB_PATH = "db/data.csv"


def load_data():
    products = []

    try:
        with open(DB_PATH, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "quantity": int(row["quantity"]),
                    "price": int(row["price"])
                })

    except FileNotFoundError:
        return []

    return products


def save_data(products):
    with open(DB_PATH, mode="w", newline="") as file:
        fieldnames = ["id", "name", "quantity", "price"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(products)