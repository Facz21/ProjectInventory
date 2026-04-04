# IMPORTS

# Import input validations for update operations
from source.validations import (
    input_valid_float, input_valid_int
)


# CRUD FUNCTIONS

def create_product(products, product_id, name, quantity, price):
    """
    Creates a new product dictionary.

    Args:
        products (list): Current list of products
        product_id (int): Unique product ID
        name (str): Product name
        quantity (int): Number of units
        price (float): Product price

    Returns:
        dict: The created product
    """
    
    product = {
        "id": product_id,
        "name": name,
        "quantity": quantity,
        "price": price
    }

    print(f"Product {name} added")
    return product


def show_products(products):
    """
    Displays all products stored in the inventory.
    """

    if not products:
        print("No products available")
        return

    for product in products: 
        for k, v in product.items():
            print(k, ":", v)
        print("--------------")


def find_product(products, product_id):
    """
    Finds a product by its ID.

    Returns:
        dict | None: Found product or None if not found
    """
    
    for product in products:
        if product["id"] == product_id:
            return product

    return None


def search_by_ID(products, product_id):
    """
    Searches and displays a product by ID.
    """

    product = find_product(products, product_id)

    if product:
        print("\nProduct found:")
        print(product)
    else:
        print("Product not found")


def search_by_name(products, product_name):
    """
    Searches a product by name (case insensitive).
    """

    for product in products:
        if product["name"].lower() == product_name.lower():
            print(f"Product found: {product}")
            return product

    
    print("Product not found")


def update_product(products, product_id):
    """
    Updates product information by ID.
    """

    product = find_product(products, product_id)

    if product:
        print("Updating product:")

        
        new_name = input(f"Name ({product['name']}): ")
        new_quantity = input_valid_int(f"Quantity ({product['quantity']}): ")
        new_price = input_valid_float(f"Price ({product['price']}): ")

        if new_name:
            product["name"] = new_name
        if new_quantity:
            product["quantity"] = new_quantity
        if new_price:
            product["price"] = new_price

        print("Product updated")

    else:
        print("Product not found")


def delete_product(products, product_id):
    """
    Deletes a product from the inventory using its ID.
    """

    product = find_product(products, product_id)

    if product:
        products.remove(product)
        print("Product deleted")
    else:
        print("Product not found")


# STATISTICS FUNCTIONS 

def get_total_units(products):
    """
    Returns total quantity of all products.
    """
    return sum(p["quantity"] for p in products)


def get_total_value(products):
    """
    Returns total inventory value (price * quantity).
    """
    return sum(p["price"] * p["quantity"] for p in products)


def get_most_expensive(products):
    """
    Returns the most expensive product.
    """
    return max(products, key=lambda p: p["price"], default=None)


def get_product_more_stock(products):
    """
    Returns the product with the highest stock.
    """
    return max(products, key=lambda p: p["quantity"], default=None)


# STATISTICS DISPLAY

def show_statistics(products):
    """
    Displays inventory statistics.
    """

    if not products:
        print("No products available")
        return

    total_units = get_total_units(products)
    total_value = get_total_value(products)
    most_expensive = get_most_expensive(products)
    more_stock = get_product_more_stock(products)

    print(f"""
================ STATISTICS ================
Total units: {total_units}
Total value: {total_value:.2f}

Most expensive product:
{most_expensive['name']} - {most_expensive['price']}

Product with more stock:
{more_stock['name']} - {more_stock['quantity']}
==========================================
""")