# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(weight) / float(height) ** 2

#Save as whole number (integer)
int_BMI = int(BMI)

#if/else statements
if int_BMI < 18.5:
    print(f"You're BMI is {int_BMI}, you are underweight.")
elif int_BMI <= 25:
    print(f"You're BMI is {int_BMI}, you are normal weight.")
elif int_BMI <= 30:
    print(f"You're BMI is {int_BMI}, you are slightly overweight.")
elif int_BMI <= 35:
    print(f"You're BMI is {int_BMI}, you are overweight.")
else:
    print(f"You're BMI is {int_BMI}, you are clinically obese.")

#############################
# Official Code

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")