def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10  
        num //= 10  
    return total

for num in range(100, 1001):
    if sum_of_digits(num) % 9 == 0:
        print(num, end=" ")
