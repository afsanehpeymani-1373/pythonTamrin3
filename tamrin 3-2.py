# tamrin 3-2
# Find The Treasure Game:
print(" wellcom to treasure island_your mission is to find the treasure ")
your_choice_1 = input(" left to right ? ")
if your_choice_1 == 'right':
    print("game over")
elif your_choice_1 == 'left':
    your_choice_2 = input(" swim to wait ? ")
    if your_choice_2 == 'siwm':
        print("game over")
    elif your_choice_2 == 'wait':
        your_choice_3 = input(" which door ? blue  red  yellow :: ")
        if your_choice_3 == "blue":
            print("game over")
        elif your_choice_3 == "red":
            print("game over")
        elif your_choice_3 == "yellow":
            print("you win")



