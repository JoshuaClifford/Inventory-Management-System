"""
Utility functions for inventory management.
Handles file operations and formatted display.
"""

def load_inventory(filename):
    """Load inventory from a text file into a dictionary."""
    inventory = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                name, qty = line.strip().split(":")
                inventory[name] = int(qty)
    except FileNotFoundError:
        pass  # File will be created later if not found
    return inventory

def save_inventory(inventory, filename):
    """Save inventory dictionary to a text file."""
    with open(filename, "w") as f:
        for name, qty in inventory.items():
            f.write(f"{name}:{qty}\n")

def display_inventory(inventory):
    """Display inventory in a formatted table."""
    if not inventory:
        print("📦 Inventory is empty.")
    else:
        print("\n--- Current Inventory ---")
        print(f"{'Item Name':<20} {'Quantity':>10}")
        print("-" * 32)
        for name, qty in inventory.items():
            print(f"{name:<20} {qty:>10}")
