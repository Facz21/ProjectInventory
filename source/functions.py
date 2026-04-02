#CRUD operations functions

def create_product(products, product_id, name, quantity, price):
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
    """
    Show all the products stored
    """
    
    for products in products:
        for k, v in products.items():
            print(k, ":", v)
        print("--------------")
    if not products:
        print("No products avalible")

def find_product(products,product_id):
    """
    Find a product based on its ID
    """
    for product in products:
        if product["id"] == product_id:
            return product
    return None

def search_by_ID(products, product_id):
    """
    Search a product by its ID and show it to the user
    
    :param products: the inventory here we store products
    :param product_id: number based unique ID
    """
    product = find_product(products, product_id)
    
    if product:
        print(f"""
Product found:
{product}              
              """)
    else:
        print("Product not found")

def search_by_name(products, product_name):
    """
    Search a product matching its name on the products inventory
    
    :param products: the inventory here we store products
    :param product_name: the product name
    """
    for product in products:
        if product["name"].lower() == product_name.lower():
            print(f"Product found: {product}")
            return product
    if product["name"].lower() != product_name.lower():
        print("Product not found")

    
def update_product(products, product_id):
    """
    Update a product information by matching  its ID and show it to the user
    
    :param products: the inventory here we store products
    :param product_id: number based unique ID
    """
    product = find_product(products, product_id)
    
    if product:
        print("Updating product: ")
        
        new_name = str(input(f"Name ({product["name"]}): "))
        new_quantity = int(input(f"Quantity ({product["quantity"]}): "))
        new_price = int(input(f"Price ({product["price"]}): "))
        
        if new_name:
            product["name"] = new_name 
        if new_quantity:
            product["quantity"] = new_quantity
        if new_price:
            product["price"] = new_price
        
        print("Product updated")
               
    else:
        print("Product not found")
        
def  delete_product(products, product_id):
    """
    Delete a product from the inventory using its ID as refference
    
    :param products: the inventory here we store products
    :param product_id: number based unique ID
    """
    product = find_product(products, product_id)
    
    if product:
        products.remove(product)
        print("Product deleted")
    
    else:
        print("Product not found")
        
#Functions to calculate statistics

def get_total_units(products):
    """
    Show all the units stored un the inventory
    """
    return sum(p["quantity"] for p in products)

def get_total_value(products):
    return sum(p["price"] * p["quantity"]for p in products)

def get_most_expensive(products):
    return max(products, key=lambda p:p["price"], default=None)

def get_product_more_stock(products):
    return max(products, key=lambda p:p["quantity"], default=None)

#main function to show statistics

def show_statistics(products):
    if not products:
        print("No products avalible")
        return
    
    total_units = get_total_units(products)
    total_value = get_total_value(products)
    most_expensive = get_most_expensive(products)
    more_stock = get_product_more_stock(products)
    
    print(f"""
================STATISTICS================
Total units: {total_units}
Total value: {total_value}

Most expensive product: 
{most_expensive["name"]} - {most_expensive["price"]}

Product with more stock:
{more_stock["name"]} - {more_stock["price"]}
==========================================         
          """)