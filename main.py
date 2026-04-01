#main route where we use all the functions of the program
from ui.menus import *
from source.functions import *
#Initializer variable
start = 1 

#This dic
products = [{'id': 1, 'name': 'Apple Juice', 'quantity': 20, 'price': 200}]
while start != 0 : #Control the program flow with a comparasion
    
    show_main_menu()
    
    option = input("Select a option: ") 
    
    if option == "1":
        product_id = int(input("Enter the product ID: "))
        name = str(input("Enter the product name: "))
        quantity = int(input("Enter the quantity of products: "))
        price = int(input("Enter the price of product: "))
        product = create_product(product_id,name,quantity,price)
        products.append(product)    
        print(products)
        
    elif option =="2":
        show_products(products)
    elif option =="3":
        print("Search Product")
    elif option == "0":
        print("Good bye user")
        start = 0
    else:
        print("")