
x = int(input("Enter base (X): "))
y = int(input("Enter exponent (Y): "))

res = 1
for i in range(y):
    res *= x

print(f"{x}^{y} = {res}")