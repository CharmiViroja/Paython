# Write a Python function to reverses a string if its length is a multiple of 4.
enterString = input("Enter a string : ")
if len(enterString) % 4 == 0:
    enterString = enterString[::-1]
else:
    enterString = enterString
print(enterString)
