def calculate_total(quantity, price):
    return quantity * price

def stock_status(quantity):
    if quantity == 0:
        return "Out of stock"
    if quantity < 10:
        return "Low stock"
    return "In stock"

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

def inventory_total(inventory):
    total = 0
    for item in inventory.values():
        total += calculate_total(item["quantity"], item["price"])
    return total

def display_inventory(inventory):
    if not inventory:               # empty dict is falsy
        print("Inventory is empty.")
        return
    for name, item in inventory.items():
        status = stock_status(item["quantity"])
        print(f"{name}: {item['quantity']} units at ₦{item['price']} ({status})")

inventory = {
    "beans": {"quantity": 50, "price": 1200},
    "garri": {"quantity": 5, "price": 800},
}

print(calculate_total(25, 1500))      # 37500
print(stock_status(0))                # Out of stock
print(stock_status(5))                # Low stock
print(stock_status(50))               # In stock
print(inventory_total(inventory))     # 64000

display_inventory(inventory)          # prints by itself
display_inventory({})                 # Inventory is empty.

price = get_float("Enter a price: ")
print(f"You entered: {price}")