# Write a Python program to check if a number is positive, negative or zero. 

for i in range (1,6):
    num = int(input("Enter number : "))
    if num % 2==0:
        print ("Even")
    else:
        print("Odd ")

for i in range (1,6):
    num = int(input("Enter number : "))
    if num < 0:
        print ("Negative")
    else:
        print("Positive")