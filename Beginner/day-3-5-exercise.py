# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names_concat = name1.lower() + name2.lower()

names_true_total = names_concat.count('t') + names_concat.count('r') + names_concat.count('u') + names_concat.count('e')
names_love_total = names_concat.count('l') + names_concat.count('o') + names_concat.count('v') + names_concat.count('e')

score_str = str(names_true_total) + str(names_love_total)
score = int(score_str)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
