### Randomization in Python!! ###

### first have to import the module by performing

import random
random_integer = random.randint(1,10)
print(random_integer)

### You can create your own modules and import by specifying in your code
### In this folder I created my_module.py and within it I created a variable for pi
### I can call that variable in this script by specifying the file name + variable

import my_module

print(my_module.pi)