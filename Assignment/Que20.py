# Write a Python function that takes a list of words and returns the length of the longest one.
myList = []
length = 0
largestWord = ''
num = int(input('How many words do you want to add in the list? : '))
for items in range(num):
    element = input(f'Enter List element {items+1}: ')
    myList.append(element)
for word in myList:
    if len(word) > length:
        length = len(word)
        largestWord = word
    else:
        length = length
print(f"The largest word is {largestWord} and the length is {length}")