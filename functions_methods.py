# functions
print('a value')
print(input('ask for a value'))

# methods -> functions of datatypes
print('value'.upper())
print('VALUE'.lower())
print('value'.replace('e', '3'))

# new functions
print(abs(-1))
print(max(10, 5))
print(min(10, 5))
print(len('test'))

# pythagoras theorem exercise
side_a = int(input('The Width of the triangle: '))
side_b = int(input('The Height of the triangle: '))
hypotenuse = float((side_a ** 2 + pow(side_b, 2)) ** (1/2))
print('The hypotenuse is:', round(hypotenuse, 2))