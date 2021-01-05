#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

random_coin = random.randint(0, 1)
#print(random_coin)
if random_coin == 1:
    print("Heads")
elif random_coin == 0:
    print("Tails")
