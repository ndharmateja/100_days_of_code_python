from random import randint

def print_rock():
    print("""\n    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\n""")


def print_paper():
    print("""\n    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)\n""")
    

def print_scissors():
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')


def print_symbol(x):
    if x == 0:
        print_rock()
    elif x == 1:
        print_paper()
    else:
        print_scissors()
        

# u c w diff diff%3
# 0 1 c  -1   2
# 1 2 c  -1   2
# 2 0 c  2    2
# 1 0 u  1    1
# 2 1 u  1    1
# 0 2 u  -2   1
def print_winner(user_input, computer_input):
    diff = (user_input - computer_input) % 3
    if diff == 1:
        print("You won!")
    elif diff == 2:
        print("You lose!")
    else:
        print("It's a draw!")


def run():
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    user_input = int(input())
    if not 0 <= user_input <= 2:
        print("You typed an invalid number, you lose!") 
        return
    computer_input = randint(0, 2)
    print_symbol(user_input)
    print("Computer chose:")
    print_symbol(computer_input)
    print_winner(user_input, computer_input)


if __name__ == "__main__":
    run()