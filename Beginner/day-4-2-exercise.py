# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Angela, Ben, Jenny, Michael, Chloe
import random

buy_meal = random.randint(0, len(names) - 1)
print(f"{names[buy_meal]} is going to buy the meal today!")

'''ANOTHER WAY
buy_meal = random.choice(names)
print(f"{buy_meal} is going to buy the meal today!")
'''