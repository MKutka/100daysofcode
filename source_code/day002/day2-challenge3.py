# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)

print(years_left)

age_in_days = 365 * int(years_left)
age_in_weeks = 52 * int(years_left)
age_in_months = 12 * int(years_left)

print(f"You have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left.")

#Official Code

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"
print(message)