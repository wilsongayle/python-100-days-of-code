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

choices = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if your_choice >= 3 or your_choice < 0:
    print("You typed an invalid number. You lose!")
else:
    print(choices[your_choice])
    print(f"Computer chose: {computer_choice}")
    print(choices[computer_choice])
    if your_choice == computer_choice:
        print("It's a tie!")
    elif your_choice == 0:
        if (computer_choice == 1):
            print("You lose")
        else:
            print("You win!")
    elif your_choice == 1:
        if (computer_choice == 2):
            print("You lose")
        else:
            print("You win!")
    else:
        if (computer_choice == 0):
            print("You lose")
        else:
            print("You win!")
