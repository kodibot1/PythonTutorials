#5 winning number
from random import randint

play_again = True

while play_again:

    winning_number = randint(1,10)

    win = False
    attempts = 1

    while win == False:

        difficulty = input("Welcome to the guessing game, choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            attempts = 10
        else :
            attempts = 5

        while attempts  > 0:
            if attempts == 0:
                print ("Game over you lose")
            user = (int(input ("Guess a number")))
            if user == winning_number:
                win = True
                retry=input(f"You win, you did it in {attempts} tries, do you want to play again y or n? ")
                if retry == "y":
                    play_again = True
                else:
                    print("Good Bye!")
                    play_again = False
            else:
                if user>winning_number:
                    print("Try Lower")
                else:
                    print("Try Higher")
                attempts = attempts - 1
            