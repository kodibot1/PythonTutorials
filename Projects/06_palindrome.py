def palindrome_tracker(word):
    if word == word[-1::-1]:
        print (f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")

word_input = input("Insert a word: ")


# print(word_input[-1::-1])

palindrome_tracker(word_input)