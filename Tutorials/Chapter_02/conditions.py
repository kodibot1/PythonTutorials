age = int(input("Insert your age: "))

if age >= 18 and age <= 119:
    print("You are eligible for voting!")
elif age > 119 or age < 1:
    print("You are an alien!")
else:
    print("You are not eligible for voting!")
