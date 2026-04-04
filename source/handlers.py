# IMPORTS

# Business logic functions (CRUD + search + statistics)
from source.functions import (
    create_product, show_products, search_by_ID,
    search_by_name, update_product, delete_product,
    show_statistics, find_product
)

# Input validations
from source.validations import input_valid_int, input_valid_float, input_unique_id

# Data persistence (CSV)
from data.csv_manager import save_data

# UI menus
from ui.menus import search_menu

# Helper utilities (clear screen and pause)
from utils.helpers import cs, p


# HANDLERS

def handle_add_product(products):
    """
    Handles the process of adding a new product.

    Steps:
    - Clears screen
    - Requests user input (ID, name, quantity, price)
    - Validates inputs
    - Creates the product
    - Appends it to the list
    - Saves data to CSV
    """

    cs()

    # Get a unique product ID
    product_id = input_unique_id(products, find_product)

    # Get product information
    name = input("Enter the product name: ")
    quantity = input_valid_int("Enter quantity: ")
    price = input_valid_float("Enter price: ")

    # Create product dictionary
    product = create_product(products, product_id, name, quantity, price)

    # If creation was successful, store and persist data
    if product:
        products.append(product)
        save_data(products)

    # Pause for user to read feedback
    p(2)


def handle_search(products):
    """
    Handles the search menu.

    Allows the user to:
    - Search by ID
    - Search by name
    - Exit back to main menu
    """

    start = 1

    while start != 0:
        cs()
        search_menu()
        option = input("Select an option: ")

        # Search by ID
        if option == "1":
            try:
                product_id = int(input("Enter ID: "))
                search_by_ID(products, product_id)
            except ValueError:
                print("Invalid ID")

        # Search by name
        elif option == "2":
            name = input("Enter name: ")
            search_by_name(products, name)

        # Exit search menu
        elif option == "0":
            start = 0

        # Invalid option
        else:
            print("Invalid option")

        p(2)


def handle_update(products):
    """
    Handles updating an existing product.

    Steps:
    - Requests product ID
    - Updates product if found
    - Saves updated data to CSV
    """

    try:
        product_id = int(input("Enter ID: "))
        update_product(products, product_id)
        save_data(products)

    except ValueError:
        print("Invalid input")

    p(2)


def handle_delete(products):
    """
    Handles deleting a product.

    Steps:
    - Requests product ID
    - Deletes product if found
    - Saves updated data to CSV
    """

    try:
        product_id = int(input("Enter ID: "))
        delete_product(products, product_id)
        save_data(products)

    except ValueError:
        print("Invalid input")

    p(2)