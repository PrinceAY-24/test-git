#Defining, calling, parameter and arguments
# def greet(name):
#     print(f"Welcome to the store, Mr/Ms. {name}")

# greet("Ada")


#Multiple parameter
# def show_item(name, quantity, price):
#     print(f"{name}: {quantity} units at ${price}")

# show_item(price=1, name="Rice", quantity=25)


#Return values
# def total_value(quantity, price):
#     return quantity * price

# result = total_value(25, 1)
# print(result)


#Returning multiple values
# def stats(numbers):
#     return min(numbers), max(numbers), sum(numbers)

# dist = stats([5, 12, 3])
# print(dist)


# Early return
# def check_quantity(qty):
#     if qty < 0:
#         return "Invalid"
#     if qty == 0:
#         return "Out of stock"
#     return "In stock"

# reserve = check_quantity(25)
# print(reserve)


#Functions in lists and dictionaries
# def add_stock(inventory, name, amount):
#     inventory[name]["quantity"] += amount

# stock = {"beans": {"quantity": 40, "price": 1}}
# add_stock(stock, "beans", 10)
# print(stock["beans"]["quantity"])

#Functions calling functions and docstrings
# def line_total(item):
#     """Return quantity * price for one item dict."""
#     return item['quantity'] * item["price"]

# def inventory_total(inventory):
#     total = 0
#     for item in inventory.values():
#         total += line_total(item)
#     return total


# #Reuseable input helper
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

# qty = get_int("Quantity: ")



#Exercise
def calculate_total(quantity, price):
    return quantity * price

result = calculate_total(quantity=20, price=3)
print(f"${result}")

def stock_status(quantity):
    if quantity == 0:
        return "Out of stock"
    if quantity < 10:
        return "Low stock"
    return "In stock"

store = stock_status(500)
print(store)

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Can't be negative.")
                continue
            return value
        except ValueError:
            print("Enter a valid number")

average = get_float("Quantity: ")


inventory = {
    "rice": {"quantity": 25, "price": 1},
    "beans": {"quantity": 40, "price": 1},
}

def inventory_total(inventory):
    total = 0
    for item in inventory.values():
        total += calculate_total(item["quantity"] * item["price"])
    return total


def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    for name, item in inventory.items():
        status = stock_status(item["quantity"])
        print(f"{name}: {item["quantity"]} units at ${item["prices"]} ({status})")