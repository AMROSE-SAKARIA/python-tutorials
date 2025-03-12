n = int(input("Enter the count of numbers: "))
even=0
odd = 0

for i in range(n):
    num = int(input(f"Enter number {i+1}: ")) 
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Evens: {even}, Odds: {odd}")