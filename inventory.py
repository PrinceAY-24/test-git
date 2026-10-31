#Data and input helpers

inventory = {}

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



#Add an item

def add_item():
    name = get_name("Item name: ")
    if name in inventory:
        print(f"'{name}' already exists. Use Update instead.")
        return
    quantity = get_int("Quantity: ")
    price = get_float("Unit price (₦): ")
    inventory[name] = {"quantity": quantity, "price": price}
    print(f"Added {name}.")



#View items

def view_items():
    if not inventory:
        print("Inventory is empty.")
        return
    print(f"\n{'Item':<15}{'Qty':>6}{'Price':>12}{'Value':>14}")
    print("-" * 47)
    grand_total = 0
    for name, item in inventory.items():
        value = item["quantity"] * item["price"]
        grand_total += value
        print(f"{name:<15}{item['quantity']:>6}{item['price']:>12,.2f}{value:>14,.2f}")
    print("-" * 47)
    print(f"{'Total':<33}{grand_total:>14,.2f}")



#Update an item

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
    print("Updated.")



#Delete an item

def delete_item():
    name = get_name("Item to delete: ")
    if name not in inventory:
        print("Item not found.")
        return
    confirm = input(f"Delete '{name}'? (y/n): ").strip().lower()
    if confirm == "y":
        del inventory[name]
        print("Deleted.")
    else:
        print("Cancelled.")



#The menu loop

def show_menu():
    print("\n=== Inventory Manager ===")
    print("1. Add item")
    print("2. View items")
    print("3. Update item")
    print("4. Delete item")
    print("5. Quit")

def main():
    actions = {
        "1": add_item,
        "2": view_items,
        "3": update_item,
        "4": delete_item,
    }
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()