# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height ** 2)

if bmi < 18.5:
  print(f"Your BMI is {int(bmi)}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {int(bmi)}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {int(bmi)}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {int(bmi)}, you are obese.")
else:
  print(f"Your BMI is {int(bmi)}, you are clinically obese.")