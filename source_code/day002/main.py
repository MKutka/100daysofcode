#Data Types

#String
#Hello is quotes is the string or output
print("Hello")

#Subscript
#looks at the position within the string and outputs just that character
#below will output just H
print("Hello"[0])

#below will output just o
print("Hello"[4])

#Integer
#actual numbers in the code for calculating
#displayed just as numbers without quotes
#below will add 123+456 = 579
print(123+456)

#in python 1000 is seperated with underscroll
#this is to make it easier to read in the code
print(1_000)
print(125_000)

#Float
#This is used for decimals
3.14159

#Boolean
#data type which is always either True or False

True
False

print(3 * (3 + 3) / 3 - 3)

#Round Numbers

#Will round into a whole number by default
print(round(8/3))

#If you want to round to two decimal places add a comma and specify which spot
print(round(8/3,2))
print(round(8/3,3))

#F Strings

#Used to print an integer/float/booleans in a string

print(f"your score is {3}")