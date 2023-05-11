# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
string = input("Enter a string : ")
stringList = string.split()
if stringList.index('not') > stringList.index('poor'):
    string = string.replace('not', 'good')
    string = string.replace('poor', 'good')
else:
    string = string
print(string)