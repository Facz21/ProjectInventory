# MAIN MENU

def show_main_menu():
    """
    Displays the main menu with numbered options.

    Each option represents a different operation in the system,
    including CRUD actions, statistics, and data persistence.
    """
    
    print("""
==============================
         MAIN MENU
==============================
1. Add product
2. Show products
3. Search product
4. Update product
5. Delete product
6. Show statistics
7. Save to CSV
8. Load from CSV
0. Exit
==============================
""")


# SEARCH MENU
def search_menu():
    """
    Displays the search submenu.

    Allows the user to choose how to search for products:
    - By ID
    - By name
    - Exit to main menu
    """
    
    print("""
==============================
        SEARCH MENU
==============================
1. Search by ID
2. Search by name
0. Exit
==============================
""")