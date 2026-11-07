# #Data and input helpers

# inventory = {}

# def get_int(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#             if value < 0:
#                 print("Can't be negative.")
#                 continue
#             return value
#         except ValueError:
#             print("Enter a whole number.")

# def get_float(prompt):
#     while True:
#         try:
#             value = float(input(prompt))
#             if value < 0:
#                 print("Can't be negative.")
#                 continue
#             return value
#         except ValueError:
#             print("Enter a valid number.")

# def get_name(prompt):
#     while True:
#         name = input(prompt).strip().lower()
#         if name:
#             return name
#         print("Name can't be empty.")



# #Add an item

# def add_item():
#     name = get_name("Item name: ")
#     if name in inventory:
#         print(f"'{name}' already exists. Use Update instead.")
#         return
#     quantity = get_int("Quantity: ")
#     price = get_float("Unit price (₦): ")
#     inventory[name] = {"quantity": quantity, "price": price}
#     print(f"Added {name}.")



# #View items

# def view_items():
#     if not inventory:
#         print("Inventory is empty.")
#         return
#     print(f"\n{'Item':<15}{'Qty':>6}{'Price':>12}{'Value':>14}")
#     print("-" * 47)
#     grand_total = 0
#     for name, item in inventory.items():
#         value = item["quantity"] * item["price"]
#         grand_total += value
#         print(f"{name:<15}{item['quantity']:>6}{item['price']:>12,.2f}{value:>14,.2f}")
#     print("-" * 47)
#     print(f"{'Total':<33}{grand_total:>14,.2f}")



# #Update an item

# def update_item():
#     name = get_name("Item to update: ")
#     item = inventory.get(name)
#     if item is None:
#         print("Item not found.")
#         return
#     print(f"Current: {item['quantity']} units at ₦{item['price']}")
#     print("1. Quantity")
#     print("2. Price")
#     choice = input("What do you want to change? ").strip()
#     if choice == "1":
#         item["quantity"] = get_int("New quantity: ")
#     elif choice == "2":
#         item["price"] = get_float("New price: ")
#     else:
#         print("Invalid choice.")
#         return
#     print("Updated.")



# #Delete an item

# def delete_item():
#     name = get_name("Item to delete: ")
#     if name not in inventory:
#         print("Item not found.")
#         return
#     confirm = input(f"Delete '{name}'? (y/n): ").strip().lower()
#     if confirm == "y":
#         del inventory[name]
#         print("Deleted.")
#     else:
#         print("Cancelled.")



# #The menu loop

# def show_menu():
#     print("\n=== Inventory Manager ===")
#     print("1. Add item")
#     print("2. View items")
#     print("3. Update item")
#     print("4. Delete item")
#     print("5. Quit")

# def main():
#     actions = {
#         "1": add_item,
#         "2": view_items,
#         "3": update_item,
#         "4": delete_item,
#     }
#     while True:
#         show_menu()
#         choice = input("Choose an option: ").strip()
#         if choice == "5":
#             print("Goodbye!")
#             break
#         action = actions.get(choice)
#         if action:
#             action()
#         else:
#             print("Invalid option.")

# if __name__ == "__main__":
#     main()


































#Updated Version

import json

DATA_FILE = "inventory.json"
LOW_STOCK_LIMIT = 10


# ---------- Saving & loading ----------
def load_inventory():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}                       # first run: no save file yet
    except json.JSONDecodeError:
        print("Save file is damaged. Starting with an empty inventory.")
        return {}


def save_inventory():
    with open(DATA_FILE, "w") as f:
        json.dump(inventory, f, indent=4)


inventory = load_inventory()


# ---------- Input helpers ----------
def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Can't be negative.")
                continue
            return value
        except ValueError:
            print("Enter a whole number.")


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Can't be negative.")
                continue
            return value
        except ValueError:
            print("Enter a valid number.")


def get_name(prompt):
    while True:
        name = input(prompt).strip().lower()
        if name:
            return name
        print("Name can't be empty.")


# ---------- Display ----------
def show_table(items):
    """Print any dict of items as a table (reused by view, search, report)."""
    print(f"\n{'Item':<15}{'Qty':>6}{'Price':>12}{'Value':>14}")
    print("-" * 47)
    grand_total = 0
    for name, item in items.items():
        value = item["quantity"] * item["price"]
        grand_total += value
        print(f"{name:<15}{item['quantity']:>6}{item['price']:>12,.2f}{value:>14,.2f}")
    print("-" * 47)
    print(f"{'Total':<33}{grand_total:>14,.2f}")


def view_items():
    if not inventory:
        print("Inventory is empty.")
        return
    show_table(inventory)


# ---------- Core actions ----------
def add_item():
    name = get_name("Item name: ")
    if name in inventory:
        print(f"'{name}' already exists. Use Update instead.")
        return
    quantity = get_int("Quantity: ")
    price = get_float("Unit price (₦): ")
    inventory[name] = {"quantity": quantity, "price": price}
    save_inventory()
    print(f"Added {name}.")


def update_item():
    name = get_name("Item to update: ")
    item = inventory.get(name)
    if item is None:
        print("Item not found.")
        return
    print(f"Current: {item['quantity']} units at ₦{item['price']}")
    print("1. Quantity")
    print("2. Price")
    choice = input("What do you want to change? ").strip()
    if choice == "1":
        item["quantity"] = get_int("New quantity: ")
    elif choice == "2":
        item["price"] = get_float("New price: ")
    else:
        print("Invalid choice.")
        return
    save_inventory()
    print("Updated.")


def delete_item():
    name = get_name("Item to delete: ")
    if name not in inventory:
        print("Item not found.")
        return
    confirm = input(f"Delete '{name}'? (y/n): ").strip().lower()
    if confirm == "y":
        del inventory[name]
        save_inventory()
        print("Deleted.")
    else:
        print("Cancelled.")


# ---------- Level-up features ----------
def sell_item():
    name = get_name("Item to sell: ")
    item = inventory.get(name)
    if item is None:
        print("Item not found.")
        return
    if item["quantity"] == 0:
        print(f"'{name}' is out of stock.")
        return
    print(f"Available: {item['quantity']}")
    amount = get_int("Quantity to sell: ")
    if amount == 0:
        print("Nothing to sell.")
        return
    if amount > item["quantity"]:
        print(f"Not enough stock. Only {item['quantity']} available.")
        return
    item["quantity"] -= amount
    save_inventory()
    print(f"Sold {amount} {name} for ₦{amount * item['price']:,.2f}.")
    if item["quantity"] < LOW_STOCK_LIMIT:
        print(f"Warning: {name} is low on stock ({item['quantity']} left).")


def search_items():
    term = input("Search for: ").strip().lower()
    if not term:
        print("Type something to search for.")
        return
    matches = {n: i for n, i in inventory.items() if term in n}
    if not matches:
        print("No items match.")
        return
    show_table(matches)


def low_stock_report():
    low = {n: i for n, i in inventory.items() if i["quantity"] < LOW_STOCK_LIMIT}
    if not low:
        print("No items are low on stock.")
        return
    print(f"\nItems with fewer than {LOW_STOCK_LIMIT} units:")
    show_table(low)


# ---------- Menu ----------
def show_menu():
    print("\n=== Inventory Manager ===")
    print("1. Add item")
    print("2. View items")
    print("3. Update item")
    print("4. Delete item")
    print("5. Sell item")
    print("6. Search items")
    print("7. Low-stock report")
    print("8. Quit")


def main():
    actions = {
        "1": add_item,
        "2": view_items,
        "3": update_item,
        "4": delete_item,
        "5": sell_item,
        "6": search_items,
        "7": low_stock_report,
    }
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "8":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()