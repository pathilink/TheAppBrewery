# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

total_height = 0
n = 0

for h in student_heights:
    n += 1
    total_height +=  h

avg_height = round(total_height / n)

print(avg_height)


