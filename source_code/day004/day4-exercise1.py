#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

coin_toss = random.randint(0,1)

if coin_toss == 0:
    print("Tails")
else:
    print("Heads")

### Official Code #### 

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")