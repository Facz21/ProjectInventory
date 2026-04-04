# Import UI functions (menus displayed to the user)
from ui.menus import show_main_menu

# Import data persistence functions (CSV handling)
from data.csv_manager import load_data, save_data

# Import handlers (each one manages a complete user action)
from source.handlers import (
    handle_add_product,
    handle_search,
    handle_update,
    handle_delete
)

# Import functions related to displaying data and statistics
from source.functions import show_products, show_statistics

# Import helper utilities (clear screen and pause)
from utils.helpers import cs, p


def main():
    """
    Main function that controls the entire program flow.
    It loads data, displays the menu, and executes actions based on user input.
    """

    # Control variable for the main loop (0 = exit program)
    start = 1 
    
    # Load existing products from CSV file into memory
    products = load_data()

    # Main program loop
    while start != 0:
        cs()  # Clear screen for better user experience
        show_main_menu()  # Display main menu options
        
        # Capture user option
        option = input("Select an option: ")

        # CRUD OPERATIONS

        # CREATE → Add a new product
        if option == "1":
            handle_add_product(products)

        # READ → Show all products
        elif option == "2":
            show_products(products)
            p(3)  # Pause for 3 seconds

        # SEARCH → Search product by ID or name
        elif option == "3":
            handle_search(products)

        # UPDATE → Modify an existing product
        elif option == "4":
            handle_update(products)

        # DELETE → Remove a product from inventory
        elif option == "5":
            handle_delete(products)

        # EXTRA FEATURES 

        # STATISTICS → Show inventory statistics
        elif option == "6":
            show_statistics(products)
            p(5)  # Pause to allow user to read data

        # SAVE → Manually save data to CSV file
        elif option == "7":
            save_data(products)
            print("Data saved")

        # LOAD → Inform user that data is loaded (already done at start)
        elif option == "8":
            print("Data loaded")

        # EXIT → End program
        elif option == "0":
            print("Goodbye")
            start = 0

        # INVALID OPTION → Handle incorrect input
        else:
            print("Invalid option")


# Entry point of the program
# Ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()