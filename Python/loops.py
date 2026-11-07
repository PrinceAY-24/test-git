# while True:
#     choice = input ("Type 'q' to quit, or anything else to continue: ")
#     if choice == "q":
#         break
#     print("You typed;", choice)

# prices = [500, 1200, 300]
# total = 0
# for p in prices:
#     total += p
# print(total)

# Part A - 5 multiplication
for i in range(1, 13):
    total = 5 * i
    print(f"5 x {i} = {total}")

# Part B - while loop
# while True:
#     entry = input("Enter a quantity (or 'done' to finish): ").strip().lower()
#     if entry == "done":
#         break
#     try:
#         total += int(entry)
#     except ValueError:
#         print("Invalid input. Enter a whole number or 'done'")
# print(f"Total: {total}")


total = 0
count = 0
largest = 0

while True:
    entry = input("Enter a quantity (or 'done' to finish): ").strip().lower()
    if entry == "done":
        break
    try:
        qty = int(entry)
        if qty < 0:
            print("Quantity can't be negative.")
            continue
    except ValueError:
        print("Invalid input. Enter a whole number or 'done'")
        continue

    total += qty
    count += 1
    if largest is not 0 or qty > largest:
        largest = qty

print(f"Total: {total} from {count} entries")
if largest is not None:
    print("Largest:", largest)