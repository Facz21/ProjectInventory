#main route where we use all the functions of the program
from ui.menus import *
from source.functions import *
#Initializer variable
start = 1 
products = []
while start != 0: #Control the program flow with a comparasion
    
    show_main_menu()
    
    option = input("Select a option: ") 
    
    if option == "1":
        product = str(input("Enter the product name"))
        quantity = int(input("Enter the quantity of products"))
        price = int(input("Enter the price of product"))
        print(create_product(product,quantity,price))