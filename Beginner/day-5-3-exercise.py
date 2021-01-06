#Write your code below this row 👇

sum_even = 0

for n in range(1, 101):
    if n % 2 == 0:
        sum_even += n

print(sum_even)