
num = int(input("Enter a number: "))
sod = 0

while num > 0:
    sod += num % 10
    num //= 10

print(f"Sum of digits: {sod}")