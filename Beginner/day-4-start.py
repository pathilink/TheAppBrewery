# https://en.wikipedia.org/wiki/Mersenne_Twister
# https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer) 

print(my_module.pi)

random_float = random.random()
print(random_float)

random_float2 = random.random() * 5
print(random_float2)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")