### Randomization in Python!! ###

### first have to import the module by performing

# import random
# random_integer = random.randint(1,10)
# print(random_integer)

# ### You can create your own modules and import by specifying in your code
# ### In this folder I created my_module.py and within it I created a variable for pi
# ### I can call that variable in this script by specifying the file name + variable

# import my_module

# print(my_module.pi)

# ### random.random() will print a random number between 0 and 1
# ### 0.000000 - 0.9999999 
# random_float = random.random()
# print(random_float)


### Lists!!! ###
### fruits = [item1, item2, item3]

states_of_america = ["georgia", "florida", "alabama", "south carolina"]

### to pull indidivudal from a list specify the index

print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[2])

### to change a variable in a list specify the existing and then update like you would any variable

states_of_america[0] = "hawaii"
print(states_of_america)

### to add you'll need to use a function to append additional items to lists

states_of_america.append("montana")
print(states_of_america)