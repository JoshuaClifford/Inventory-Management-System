"""
Inventory Management System
Author: Joshua Ibitamuno Clifford
Description: A simple command-line inventory system to add, delete,
update, search, and display items. Data is persisted in a text file.
"""

from utils import load_inventory, save_inventory, display_inventory

DATA_FILE = "inventory_data.txt"

def add_item(inventory):
    try:
        item_name = input("Enter item name: ").strip().title()
        quantity = int(input("Enter quantity: "))
        if item_name in inventory:
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity
        print(f"✅ '{item_name}' added/updated successfully.")
    except ValueError:
        print("❌ Quantity must be a number.")

def delete_item(inventory):
    item_name = input("Enter item name to delete: ").strip().title()
    if item_name in inventory:
        del inventory[item_name]
        print(f"✅ '{item_name}' deleted.")
    else:
        print("❌ Item not found.")

def update_quantity(inventory):
    try:
        item_name = input("Enter item name to update: ").strip().title()
        if item_name in inventory:
            new_qty = int(input("Enter new quantity: "))
            inventory[item_name] = new_qty
            print(f"✅ '{item_name}' updated successfully.")
        else:
            print("❌ Item not found.")
    except ValueError:
        print("❌ Quantity must be a number.")

def search_item(inventory):
    search = input("Enter item name to search: ").strip().title()
    if search in inventory:
        print(f"🔎 {search}: {inventory[search]} units")
    else:
        print("❌ Item not found.")

def main():
    print("===== Inventory Management System =====")
    inventory = load_inventory(DATA_FILE)

    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Delete Item")
        print("3. Update Quantity")
        print("4. Search Item")
        print("5. Display Inventory")
        print("6. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            delete_item(inventory)
        elif choice == "3":
            update_quantity(inventory)
        elif choice == "4":
            search_item(inventory)
        elif choice == "5":
            display_inventory(inventory)
        elif choice == "6":
            save_inventory(inventory, DATA_FILE)
            print("✅ Inventory saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
