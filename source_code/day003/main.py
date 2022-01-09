# water_level = int(input("Please enter water level! "))
# if water_level > 80:
#     print("Drain Water")
# else:
#     print("keep filling water")

# print("welcome to the rollercoaster")
# height = int(input("What is your height? "))

# if height >= 120:
#     print("you can ride the rollercoaster")
# else:
#     print("sorry you're not allowed to ride")

# #Nested if / else statements for multiple conditions
# height = int(input("What is your height? "))

# if height >= 120:
#     print("you can ride the rollercoaster")
#     age = int(input("Hello, how old are you? "))
#     if age <= 18:
#         print("please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("sorry you're not allowed to ride")


# You can also have multiple if else statements in the same code block call if you have multiple requirements

# height = int(input("What is your height? "))

# if height >= 120:
#     print("you can ride the rollercoaster")
#     age = int(input("Hello, how old are you? "))
#     if age < 12:
#         print("please pay $5")
#     elif age <= 18:
#         print("please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("sorry you're not allowed to ride")

# Multiple If Statements in Succession

# if condition1:
#     do A
# if condition 2:
#     do B
# if condition 3:
#     do C

height = int(input("What is your height? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("Hello, how old are you? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    
    want_photo = input("Do you want a photo taken? Y or N? ")
    if want_photo == "Y":
        #adds $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("sorry you're not allowed to ride")

## Logical Operators
# Uses Boolean to identify
# A and B
# C or D
# not E