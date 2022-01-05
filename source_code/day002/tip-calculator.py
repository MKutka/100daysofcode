#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 0.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#Get the total of the bill and convert to float (as bill can have decimals)
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
bill_as_float = float(bill)

#Get tip percent and convert to decimal/float from string
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_percentage = int(tip_percent) / 100

#Determine total tip amount for bill
total_tip_amount = bill_as_float * tip_percentage

#Add Bill and Tip for total bill amount
total_bill_amount = total_tip_amount + bill_as_float

#Determine how many people the bill will be split by and save as integer
split = input("How many people to split the bill? ")
split_as_int = int(split)

amount =  total_bill_amount / split_as_int
final = round(amount,2)
final = "{:.2f}".format(amount)
print(f"Each person should pay: ${final}")

#Official Code

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay: ${final_amount}")

