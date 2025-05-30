import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

x = b ** 2 - 4 * a * c

if x > 0:
    root1 = (-b + math.sqrt(x)) / (2 * a)
    root2 = (-b - math.sqrt(x)) / (2 * a)
    print(f"Roots are real and different: {root1:.2f}, {root2:.2f}")
elif x == 0:
    root = -b / (2 * a)
    print(f"Roots are real and same: {root:.2f}")
else:
    print("No real roots")