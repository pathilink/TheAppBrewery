import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

'''
Rules:
* Rock wins against scissors.
* Scissors win against paper.
* Paper wins against rock.
'''
img = [rock, paper, scissors]

computer_choice = random.randint(0, 2)

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

if your_choice < 0 or your_choice >=3:
    print("Your choice is invalid. You lose!")
else:
    print("You chose:")
    print(img[your_choice])
    print("Computer chose:")
    print(img[computer_choice])
    if your_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and your_choice == 2:
        print("Computer win!")
    elif computer_choice == your_choice:
        print("It's a draw.")
    elif your_choice > computer_choice:
        print("You win!")
    elif computer_choice > your_choice:
        print("Computer win!")
    


'''
if your_choice == 0:
    if computer_choice == 0:
        print("You chose:")
        print(rock)
        print("Computer chose:")
        print(rock)
        print("It's a draw.")
    elif computer_choice == 1:
        print("You chose:")
        print(rock)
        print("Computer chose:")
        print(paper)
        print("Computer win!")        
    elif computer_choice == 2:
        print("You chose:")
        print(rock)
        print("Computer chose:")
        print(scissors)
        print("You win!")
elif your_choice == 1:
    if computer_choice == 0:
        print("You chose:")
        print(paper)
        print("Computer chose:")
        print(rock)
        print("You win!")
    elif computer_choice == 1:
        print("You chose:")
        print(paper)
        print("Computer chose:")
        print(paper)
        print("It's a draw.")
    elif computer_choice == 2:
        print("You chose:")
        print(paper)
        print("Computer chose:")
        print(scissors)
        print("Computer win!")
elif your_choice == 2:
    if computer_choice == 0:
        print("You chose:")
        print(scissors)
        print("Computer chose:")
        print(rock)
        print("Computer win!")
    elif computer_choice == 1:
        print("You chose:")
        print(scissors)
        print("Computer chose:")
        print(paper)
        print("You win!")
    elif computer_choice == 2:
        print("You chose:")
        print(scissors)
        print("Computer chose:")
        print(scissors)
        print("It's a draw.")
'''
