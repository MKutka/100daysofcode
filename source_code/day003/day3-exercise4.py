# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

pizza = 0

if size == "S":
    pizza = 15
    if add_pepperoni == "Y":
        pizza += 2
    if extra_cheese == "Y":
        pizza += 1
    print(f"Your final bill is : ${pizza}")
elif size == "M":
    pizza = 20
    if add_pepperoni == "Y":
        pizza += 3
    if extra_cheese == "Y":
        pizza += 1
    print(f"Your final bill is : ${pizza}")
elif size == "L":
    pizza = 25
    if add_pepperoni == "Y":
        pizza += 3
    if extra_cheese == "Y":
        pizza += 1
    print(f"Your final bill is : ${pizza}")

## Official Code

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")
