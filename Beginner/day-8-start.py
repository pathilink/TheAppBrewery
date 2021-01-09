# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Simple function--------------------------------------------
def greet():
    print("Hello")
    print("gals!")
    print("Girl Power! 💪")

greet()


# Function that allows for input-----------------------------

def greet_with_name(name):
    print(f"Hello {name}!")
    print("How are you?")
    print("Girl Power! 💪")

#parameter (name of data) = argument (value of data)
ladie = "Ada"
greet_with_name(ladie)


# Function with more than 1 input----------------------------

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"How is the weather in {location}?")

greet_with("Ada", "England")
# Positional Argument
greet_with("England", "Ada")


# Function with keyword arguments----------------------------

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"How is the weather in {location}?")

greet_with(location="England", name="Ada")