l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = list(map(lambda x: x**3, l))
print(*x)
xx = list(filter(lambda x: x>5, l))
print(*xx)

from functools import reduce
mult = reduce(lambda x, y: x * y, l)
print(mult)

fruits = ["apple", "banana"]
prices = [150, 200]

for i, fruit in enumerate(fruits):
    print(f"{i}:{fruit}")

for f, p in zip(fruits, prices):
    print(f"Price of {f} is {p} TG")

a = "123"
print(type(a))
a = int(a)
print(type(a))