#main route where we use all the functions of the program
from ui.menus import *
from source.functions import *
from db.json_manager import *
#Initializer variable
start = 1 

#This dic
products = load_data()
while start != 0 : #Control the program flow with a comparasion
    
    show_main_menu()
    
    option = input("Select a option: ") 
    
    if option == "1":
       menu_options_1 = 1
       while menu_options_1 !=0: 
        try:
            sub_menu = 1
            while sub_menu != 0:
                product_id = int(input("Enter the product ID: "))
                if find_product(products, product_id):
                    print("ID already exist try another one")
                else:
                    sub_menu = 0
            name = str(input("Enter the product name: "))
            quantity = int(input("Enter the quantity of products: "))
            price = int(input("Enter the price of product: "))
            product = create_product(products,product_id,name,quantity,price)
            if product:
                products.append(product)
            menu_options_1 = 0    
        except ValueError:
            print("Invalid entry try again")
    elif option =="2":
        show_products(products)
    elif option =="3":
        menu_options_3 = 1
        while menu_options_3 != 0:
            
            search_menu()
            option = input("Select a option: ")
            if option == "1":
                product_id = int(input("Enter the product ID: "))
                search_by_ID(products, product_id)
            elif option == "2":
                product_name = input("Enter the product name: ")
                search_by_name(products,product_name)
            elif option == "0":
                print("Returning to the main menu")
                menu_options_3 = 0
            else:
                print(f"Option {option} is invalid, try again")
    elif option =="4":
        menu_options_4 = 1
        while menu_options_4 != 0:
            try:
                product_id = int(input("Enter the product ID: "))
                update_product(products, product_id)
                menu_options_4 = 0
            except ValueError:
                print("Enter a valid data")

    elif option == "5":
        menu_options_5 = 1
        while menu_options_5 != 0:
            try:
                product_id = int(input("Enter the product ID: "))
                delete_product(products, product_id)
                menu_options_5 = 0
            except ValueError:
                print("Enter a valid data for ID")
    elif option == "6":
        show_statistics(products)
    elif option == "7":
        save_data(products)
        print("Data saved successfully")    
    elif option == "8":
        load_data()
        print("Data load successfully")
    elif option == "0":
        print("Good bye user")
        start = 0
    else:
        print("")
        