# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
enterString = input("Enter a string : ")
firstTwo = enterString[0:2]
lastTwo = enterString[-2:]
if len(enterString) < 2:
    print(enterString)
else:
    enterString = firstTwo + lastTwo
    print(enterString)