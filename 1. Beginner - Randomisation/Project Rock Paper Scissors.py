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

opcion = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if opcion == 1:
  print(rock)
elif opcion == 2:
  print(paper)
elif opcion == 3:
  print(scissors)
else:
  print("Option not selected")

pc = random.randint(1,3)
if pc == 1:
  print(f"Computer chose:\n {rock}")
elif pc == 2:
  print(f"Computer chose:\n {paper}")
else:
  print(f"Computer chose:\n {scissors}")

if (opcion == 1 and pc == 3) or (opcion == 2 and pc == 1) or (opcion == 3 and pc == 2):
  print("You win!")
elif (opcion == 1 and pc == 1) or (opcion == 2 and pc == 2) or (opcion == 3 and pc == 3):
  print("It's a draw")
else:
  print("You lose")