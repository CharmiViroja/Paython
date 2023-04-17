"""

looping example :
there are two types of Loop

1) for loop : for loop - sequence contrl loop
2)while loop : while loop : entry controlled loop

        -> condition check at entry level
        if condition goes true loop will execute
"""


"""
while loop :
    syntax :
    intialization

    while condition:
        statement
        updation

"""

for i in range(5): #by default loop start from 0 to 4
    print(i)

for i in range(1,6): #by default loop start from 1 to 5
    print(i)

# accept 5 numbers from user
for i in range (1,6):
    num = int(input("Enter number : "))

# accept 5 numbers from user and sum
sum= 0
for i in range (1,6):
    num = int(input("Enter number : "))
    sum += num

print("ans = ",sum)


status = True
while status:
    num = int(input("Enter number : "))
    choice =int(input("Do you want to continue press 1 for yes and pres 2 for no : "))
    if choice ==1:
        status = True
    else:
        status = False