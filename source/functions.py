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
    print(f"Product {name} added")
    return product

def show_products(products):
    
    for products in products:
        for k, v in products.items():
            print(k, ":", v)
        print("--------------")

