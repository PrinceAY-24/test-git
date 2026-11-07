# items = ["Rice", "Beans", "Spaghetti"]

# for n, item in enumerate(items, start=1):
#     print(f"{n}. {item}")

shopping = ["Rice", "Beans", "Garri"]

shopping.append("Yam")
print(shopping)

shopping.insert(1, "Oil")
print(shopping)

shopping.remove("Beans")
print(shopping)

shopping.sort()
print(shopping)

for a, food in enumerate(shopping, start=1):
    print(f"{a}. {food}")

print("The Shopping has only", len(shopping), "foods")


prices = [500, 1200, 300, 800]
high_prices = [i for i in prices if i >= 400]
# high_prices.sort()
# print(sorted(high_prices, reverse=True))
print(sorted(high_prices))