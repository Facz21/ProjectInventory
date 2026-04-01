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

def searh_by_name(products, product_name):
    for product in products:
        if product["name"].lower() == product_name.lower():
            print(f"Product found: {product}")
            return product
    print("Product not found")
    return None