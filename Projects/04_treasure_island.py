move = input("Welcome to treasure Island, Do you go Left or Right: ")
if move == "left":
    w_o_s=input ("Do you wait or swim? ")
    if w_o_s=="wait":
        door=input("You come to three doors red, yellow, blue which do you open? Type the color: ")
        if door=="yellow":
            print ("You win")
        else:
            print ("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
