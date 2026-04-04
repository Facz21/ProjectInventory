# INPUT VALIDATIONS

def input_valid_int(message):
    """
    Validates integer input from the user.

    Ensures:
    - The value is an integer
    - The value is not negative

    Args:
        message (str): Prompt message shown to the user

    Returns:
        int: A valid non-negative integer
    """
    
    start = 1
    while start != 0:
        try:
            value = int(input(message))

            if value < 0:
                print("Value cannot be negative")
            else:
                return value    

        except ValueError:
            print("Enter a valid integer value")


def input_valid_float(message):
    """
    Validates float input from the user.

    Ensures:
    - The value is a number (float)
    - The value is greater than 0

    Args:
        message (str): Prompt message shown to the user

    Returns:
        float: A valid positive number
    """
    
    start = 1
    while start != 0:
        try:
            value = float(input(message))

            if value <= 0:
                print("Price must be greater than 0")
            else:
                return value  

        except ValueError:
            print("Enter a valid number for price")


def input_unique_id(products, find_product):
    """
    Prompts the user to enter a unique product ID.

    Ensures:
    - The ID is an integer
    - The ID does not already exist in the product list

    Args:
        products (list): Current list of products
        find_product (function): Function used to search for a product by ID

    Returns:
        int: A unique product ID
    """

    start = 1
    while start != 0:
        try:
            product_id = int(input("Enter the product ID: "))

            if find_product(products, product_id):
                print("ID already exists, try another one")
            else:
                return product_id

        except ValueError:
            print("Enter a valid integer for ID")