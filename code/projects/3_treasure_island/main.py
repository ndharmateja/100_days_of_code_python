def welcome():
    print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")


def win_direction():
    left_right = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n')
    if left_right == "right":
        print("You fell into a hole. Game Over.")
        return False
    if left_right != "left":
        print("You chose an option that doesn't exist. Game Over.")
        return False
    return True


def win_swim():
    swim_wait = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if swim_wait == "swim":
        print("You get attacked by an angry trout. Game Over.")
        return False
    if swim_wait != "wait":
        print("You chose an option that doesn't exist. Game Over.")
        return False
    return True


def play_door():
    door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
    if door == "red":
        return print("It's a room full of fire. Game Over.")
    if door == "blue":
        return print("You enter a room of beasts. Game Over.")
    if door != "yellow":
        return print("You chose a door that doesn't exist. Game Over.")
    print("You found the treasure! You Win!")


def play():
    if not win_direction():
        return
    if not win_swim():
        return
    play_door()
    
    
def run():
    welcome()
    play()

if __name__ == "__main__":
    run()