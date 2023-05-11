# Write a Python program to count the occurrences of each word in a given sentence
myStr = input("Enter a string : ")
list = []
list = myStr.split()
for p in list:
    frequency = [list.count(p)]
print(dict(zip(list, frequency)))

