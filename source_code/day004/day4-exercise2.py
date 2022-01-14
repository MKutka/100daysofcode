import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

random_name = random.choice(names)

print(f"{random_name} is going to buy the meal today!")

### Official Code ###

#Get the total number of items in list.
list_length = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, list_length - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

### Shorter Code

import random

random_name = random.randint(0, (len(names)-1))

print(names[random_name] + " is going to buy the meal today!")