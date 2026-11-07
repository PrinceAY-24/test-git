qty = int(input("Quantity remaining: "))
message1 = "Out of stock"
message2 = "Low stock"
message3 = "Well stocked"
message4 = "Overstocked"
warning = "invalid quantity"

if qty < 0:
    print(f"{warning}, Admin")
elif qty == 0:
    print(f"{message1}, Admin")
elif qty < 10:
    print(f"{message2}, Admin")
elif qty < 100:
    print(f"{message3}, Admin")
else:
    print(f"{message4}, Admin")