# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

total_t = lower_case_name1.count("t") + lower_case_name2.count("t")
total_r = lower_case_name1.count("r") + lower_case_name2.count("r")
total_u = lower_case_name1.count("u") + lower_case_name2.count("u")
total_e = lower_case_name1.count("e") + lower_case_name2.count("e")

true_total = total_t + total_r + total_u + total_e

total_l = lower_case_name1.count("l") + lower_case_name2.count("l")
total_o = lower_case_name1.count("o") + lower_case_name2.count("o")
total_v = lower_case_name1.count("v") + lower_case_name2.count("v")

love_total = total_l + total_o + total_v + total_e

score = str(true_total) + str(love_total)
int_score = int(score)

if (int_score > 90) or (int_score < 10):
    print(f"Your score is {int_score}, you go together like coke and mentos")
elif (int_score > 40) and (int_score < 50):
    print(f"Your score is {int_score}, you are alright together.")
else:
    print(f"Your score is {int_score}.")

### Official Code ###

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

