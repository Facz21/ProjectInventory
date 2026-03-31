def create_product(product_id, name, quantity, price):
    """
    Creates a new product in the inventory and its ID
    """
    product = {
        "id" : product_id,
        "name" : name,
        "quantity" : quantity,
        "price" : price
    }
    return product 