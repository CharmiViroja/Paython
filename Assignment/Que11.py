# Write a python program to sum of the first n positive integers.

n = int(input("Enter a number : "))
sum = 0
for n in range(0, n+1, 1):
    sum = sum + n
print(f"{sum}")
