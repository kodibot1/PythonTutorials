import random 
lives=7
randomize=True
display=[]
while randomize==True:
    random_words=["afforest","aftermath","becalm","broadsheet","buffoonish","caprice","capricious","causerie","chivalrous","dapper","debonaire"]
    chosen_word=(random_words[random.randint(0,10)])
    randomize=False
while lives>0:
    length_cw=(len(chosen_word))
    print(f" The answer is : {chosen_word}")
    for under_score in range(length_cw):
        display.append("_")
    print(display)
    guess=input("welcome to hang-man please enter your guess")
    letters=list(chosen_word)
    if guess in letters:
        print(f" {guess} is in the chosen word")
    else:
        print(f" {guess} was not in the chosen word, you have {lives} guesses left")
        lives-1