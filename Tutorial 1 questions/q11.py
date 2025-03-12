
n = int(input("Enter a positive integer: "))
cube = 0
for i in range(2, n+1, 2):
    cube = cube + i**3

print(f"Sum of cubes of even numbers: {cube}")