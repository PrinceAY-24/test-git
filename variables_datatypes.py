product_name = str(input("Item name: "))
product_qty = int(input("item quantity: "))
product_priceperunit = float(input("Item Price Per Unit: "))
total = product_qty * product_priceperunit
print(f"{product_name}: {product_qty} units x ${product_priceperunit} = ${total}")