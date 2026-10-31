class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.quantity * self.price

    def restock(self, amount):
        self.quantity += amount

    def sell(self, amount):
        if amount > self.quantity:
            return False          # not enough stock
        self.quantity -= amount
        return True

    def status(self):
        if self.quantity == 0:
            return "Out of stock"
        if self.quantity < 20:
            return "Low stock"
        return "In stock"

    def __str__(self):
        return f"{self.name}: {self.quantity} units at ₦{self.price}"



class Inventory:
    def __init__(self):
        self.items = {}               # name -> Item object

    def add_item(self, item):
        self.items[item.name.lower()] = item

    def get_item(self, name):
        return self.items.get(name.lower())

    def remove_item(self, name):
        return self.items.pop(name.lower(), None)

    def total_value(self):
        return sum(item.total_value() for item in self.items.values())

    def display(self):
        if not self.items:
            print("Inventory is empty.")
            return
        for item in self.items.values():
            print(f"{item} ({item.status()})")


store = Inventory()
store.add_item(Item("Rice", 25, 1500))
store.add_item(Item("Beans", 40, 1200))
store.add_item(Item("Garri", 15, 800))

store.get_item("rice").restock(10)
print(store.get_item("beans").sell(100))
print(store.get_item("beans").sell(5))
store.remove_item("garri")
store.display()


class PerishableItem(Item):
    def __init__(self, name, quantity, price, expiry_days):
        super().__init__(name, quantity, price)   # run the parent's setup
        self.expiry_days = expiry_days

    def __str__(self):
        return f"{super().__str__()} (expires in {self.expiry_days} days)"

milk = PerishableItem("Milk", 12, 900, 5)
print(milk)
print(milk.total_value())