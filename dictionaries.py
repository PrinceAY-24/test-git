inventory = {
    "rice": {"quantity": 25, "price": 1},
    "beans": {"quantity": 40, "price": 1},
}

inventory["garri"] = {"quantity": 15, "price": 0.5}
print(inventory)

inventory["beans"]["quantity"] += 10
print(inventory)

del inventory["rice"]
print(inventory)

for name, details in inventory.items():
    print(f"{name}: {details['quantity']} units @ ${details['price']} each")

initial_value = 0
total_value = 0
for name, details in inventory.items():
    initial_value = details['quantity'] * details['price']
    print(f"{name}: ${initial_value}")
    total_value += initial_value
print(f"Total value: ${total_value}")

if inventory.get("yam") is None:
    print("Item not found")

name = input("Item name: ").strip().lower()
food_item = inventory.get(name)
if food_item is None:
    print("Item not found")
else:
    print(f"{name}: {details['quantity']} units @ ${details['price']}")