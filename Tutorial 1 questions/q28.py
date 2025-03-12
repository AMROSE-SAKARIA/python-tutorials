low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))


sum_odd = 0
for num in range(low, high + 1):
    if num % 2 != 0:
        sum_odd += num

print(f"Sum of odd numbers: {sum_odd}")