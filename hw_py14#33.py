"""
INTERACTIVE INVENTORY MANAGEMENT SYSTEM - STUDENT PROJECT
========================================================

PROJECT OVERVIEW:
Create an interactive inventory management system that allows users to manage 
a collection of items. Students will implement various functions to manipulate 
inventory data and create a user-friendly interface.

BASE INVENTORY DATA:
Start with the provided dictionary as your base inventory with 8 pre-loaded items
across different categories (Electronics, Office, Kitchen, Furniture).

REQUIRED FUNCTIONS:

1. display_inventory(inventory)
   - Purpose: Show all items in a formatted table
   - Parameters: inventory (dictionary)
   - Returns: Nothing (prints to console)
   - Features: Display item name, quantity, price, category in columns
     Calculate and show total inventory value
     Handle empty inventory gracefully

2. add_item_to_inventory(inventory, item_name, quantity, price, category)
   - Purpose: Add new items or update existing ones
   - Parameters: inventory, item_name, quantity, price, category
   - Returns: Updated inventory dictionary
   - Logic: If item exists, add to existing quantity
     If item is new, create new entry
     Provide user feedback about the action

3. remove_item_from_inventory(inventory, item_name, quantity)
   - Purpose: Remove items from inventory
   - Parameters: inventory, item_name, quantity
   - Returns: Updated inventory dictionary
   - Logic: Check if item exists, verify sufficient quantity
     Remove items and delete entry if quantity becomes 0
     Provide appropriate error messages

4. search_inventory(inventory, search_term)
   - Purpose: Find items by name or category
   - Parameters: inventory, search_term
   - Returns: Nothing (prints results to console)
   - Features: Search in both item names and categories
     Case-insensitive search, display matching items

5. get_category_summary(inventory)
   - Purpose: Show inventory statistics by category
   - Parameters: inventory
   - Returns: Nothing (prints summary to console)
   - Features: Group items by category, count total items per category
     Calculate total value per category

6. show_menu()
   - Purpose: Display the main menu options
   - Parameters: None
   - Returns: Nothing (prints menu to console)
   - Menu Options: 1-View Inventory, 2-Add Item, 3-Remove Item
     4-Search Items, 5-Category Summary, 6-Exit

7. main()
   - Purpose: Run the interactive program loop
   - Parameters: None
   - Returns: Nothing
   - Features: Initialize base inventory, display welcome message
     Run continuous menu loop, handle user input
     Provide input validation, show final inventory before exiting

PROGRAM FLOW REQUIREMENTS:
1. Start: Display welcome message and show base inventory has 8 items
2. Menu Loop: Continuously show menu and get user choice
3. Input Validation: Check for valid menu choices and data types
4. User Feedback: Provide clear messages for all actions (success/error)
5. Error Handling: Gracefully handle invalid inputs and edge cases
6. Exit: Show final inventory status before closing

TECHNICAL REQUIREMENTS:
- Functions: Must use all 7 required functions
- Parameters: Functions should accept appropriate parameters
- Return Values: Functions should return meaningful values when needed
- Default Parameters: Use default parameters where appropriate
- Docstrings: Include proper documentation for each function
- Input Validation: Check user inputs for validity
- User Experience: Clear prompts and feedback messages

TESTING SCENARIOS:
- Add a new item (e.g., "Wireless Keyboard" at $45.99 in "Electronics")
- Remove items from existing inventory
- Search for items by name or category
- View category summaries
- Handle invalid inputs gracefully
- Exit and see final inventory status

LEARNING OBJECTIVES:
- Function Design: Creating functions with appropriate parameters and return values
- Data Manipulation: Working with nested dictionaries and lists
- User Input: Handling various types of user input safely
- Error Handling: Managing edge cases and invalid inputs
- Program Flow: Creating interactive loops and menus
- Data Validation: Ensuring data integrity and user experience

BONUS CHALLENGES:
- Add inventory export/import functionality
- Implement low stock warnings
- Add item modification (change price/category)
- Create inventory reports with date stamps
- Add sorting options (by name, price, category)
"""

# Base inventory data - DO NOT MODIFY THIS SECTION
inventory = {
    "Laptop": {"quantity": 5, "price": 999.99, "category": "Electronics"},
    "Mouse": {"quantity": 15, "price": 25.50, "category": "Electronics"},
    "Notebook": {"quantity": 50, "price": 5.99, "category": "Office"},
    "Pen": {"quantity": 100, "price": 1.99, "category": "Office"},
    "Coffee Mug": {"quantity": 20, "price": 12.99, "category": "Kitchen"},
    "Desk Lamp": {"quantity": 8, "price": 45.00, "category": "Furniture"},
    "USB Cable": {"quantity": 25, "price": 8.99, "category": "Electronics"},
    "Paper Clips": {"quantity": 200, "price": 0.99, "category": "Office"}
}

# TODO: IMPLEMENT THE FOLLOWING FUNCTIONS

def display_inventory(inventory):
    """
    Display the current inventory in a formatted way.
    
    Args:
        inventory (dict): Current inventory dictionary
        
    Returns:
        None: Prints formatted inventory to console
    """
    # YOUR CODE HERE
    pass

def add_item_to_inventory(inventory, item_name, quantity, price, category):
    """
    Add a new item or update existing item in inventory.
    
    Args:
        inventory (dict): Current inventory dictionary
        item_name (str): Name of the item
        quantity (int): Quantity to add
        price (float): Price per unit
        category (str): Category of the item
        
    Returns:
        dict: Updated inventory dictionary
    """
    # YOUR CODE HERE
    pass

def remove_item_from_inventory(inventory, item_name, quantity):
    """
    Remove items from inventory.
    
    Args:
        inventory (dict): Current inventory dictionary
        item_name (str): Name of the item to remove
        quantity (int): Quantity to remove
        
    Returns:
        dict: Updated inventory dictionary
    """
    # YOUR CODE HERE
    pass

def search_inventory(inventory, search_term):
    """
    Search for items in inventory by name or category.
    
    Args:
        inventory (dict): Current inventory dictionary
        search_term (str): Term to search for
        
    Returns:
        None: Prints search results to console
    """
    # YOUR CODE HERE
    pass

def get_category_summary(inventory):
    """
    Show summary of inventory by category.
    
    Args:
        inventory (dict): Current inventory dictionary
        
    Returns:
        None: Prints category summary to console
    """
    # YOUR CODE HERE
    pass

def show_menu():
    """
    Display the main menu options.
    
    Returns:
        None: Prints menu to console
    """
    # YOUR CODE HERE
    pass

def main():
    """
    Main function to run the interactive inventory system.
    """
    # YOUR CODE HERE
    pass

# Test your implementation by running this file
if __name__ == "__main__":
    main() 

def display_inventory(inventory):
    """
    Display the current inventory in a formatted way.
    """
    if not inventory:
        print("\nInventory is empty.\n")
        return

    print("\nCurrent Inventory:")
    print("-" * 75)
    print(f"{'Item':20} {'Qty':>5} {'Price':>10} {'Category':15} {'Value':>10}")
    print("-" * 75)

    total_value = 0
    for item, data in inventory.items():
        value = data["quantity"] * data["price"]
        total_value += value
        print(f"{item:20} {data['quantity']:>5} "
              f"${data['price']:>9.2f} {data['category']:15} "
              f"${value:>9.2f}")

    print("-" * 75)
    print(f"{'Total Inventory Value':>60} : ${total_value:.2f}\n")


def add_item_to_inventory(inventory, item_name, quantity, price, category):
    """
    Add a new item or update existing item in inventory.
    """
    if quantity <= 0 or price < 0:
        print("Error: Quantity must be positive and price cannot be negative.")
        return inventory

    if item_name in inventory:
        inventory[item_name]["quantity"] += quantity
        inventory[item_name]["price"] = price
        inventory[item_name]["category"] = category
        print(f"Updated '{item_name}' quantity by {quantity}.")
    else:
        inventory[item_name] = {
            "quantity": quantity,
            "price": price,
            "category": category
        }
        print(f"Added new item '{item_name}' to inventory.")

    return inventory


def remove_item_from_inventory(inventory, item_name, quantity):
    """
    Remove items from inventory.
    """
    if item_name not in inventory:
        print("Error: Item not found in inventory.")
        return inventory

    if quantity <= 0:
        print("Error: Quantity to remove must be positive.")
        return inventory

    if quantity > inventory[item_name]["quantity"]:
        print("Error: Not enough quantity to remove.")
        return inventory

    inventory[item_name]["quantity"] -= quantity

    if inventory[item_name]["quantity"] == 0:
        del inventory[item_name]
        print(f"'{item_name}' has been completely removed from inventory.")
    else:
        print(f"Removed {quantity} of '{item_name}'.")

    return inventory


def search_inventory(inventory, search_term):
    """
    Search for items in inventory by name or category.
    """
    print(f"\nSearch Results for '{search_term}':")
    print("-" * 50)

    found = False
    search_term = search_term.lower()

    for item, data in inventory.items():
        if (search_term in item.lower() or
                search_term in data["category"].lower()):
            print(f"{item} | Qty: {data['quantity']} | "
                  f"Price: ${data['price']:.2f} | "
                  f"Category: {data['category']}")
            found = True

    if not found:
        print("No matching items found.")

    print()


def get_category_summary(inventory):
    """
    Show summary of inventory by category.
    """
    if not inventory:
        print("\nInventory is empty.\n")
        return

    summary = {}

    for data in inventory.values():
        cat = data["category"]
        value = data["quantity"] * data["price"]

        if cat not in summary:
            summary[cat] = {"items": 0, "value": 0}

        summary[cat]["items"] += data["quantity"]
        summary[cat]["value"] += value

    print("\nCategory Summary:")
    print("-" * 50)
    for cat, data in summary.items():
        print(f"{cat:15} Items: {data['items']:5} "
              f"Total Value: ${data['value']:.2f}")
    print()


def show_menu():
    """
    Display the main menu options.
    """
    print("Inventory Management Menu")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Search Items")
    print("5. Category Summary")
    print("6. Exit")


def main():
    """
    Main function to run the interactive inventory system.
    """
    print("=" * 50)
    print("WELCOME TO THE INVENTORY MANAGEMENT SYSTEM")
    print("Base inventory loaded with 8 items.")
    print("=" * 50)

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                display_inventory(inventory)

            elif choice == "2":
                name = input("Item name: ").strip()
                qty = int(input("Quantity: "))
                price = float(input("Price: "))
                category = input("Category: ").strip()
                add_item_to_inventory(inventory, name, qty, price, category)

            elif choice == "3":
                name = input("Item name to remove: ").strip()
                qty = int(input("Quantity to remove: "))
                remove_item_from_inventory(inventory, name, qty)

            elif choice == "4":
                term = input("Enter name or category to search: ").strip()
                search_inventory(inventory, term)

            elif choice == "5":
                get_category_summary(inventory)

            elif choice == "6":
                print("\nFinal Inventory Status:")
                display_inventory(inventory)
                print("Thank you for using the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please select 1-6.")

        except ValueError:
            print("Input error: Please enter valid numeric values where required.")
