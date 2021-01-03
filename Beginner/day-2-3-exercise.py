# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)

x = years_left * 365 # days
y = years_left * 52  # weeks
z = years_left * 12  # months

print(f"You have {x} days, {y} weeks, and {z} months left.")