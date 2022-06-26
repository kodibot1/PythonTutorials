print("Welcome to the tip calculator")
bill = int(input("What was the total bill?"))
tip = int(input("How much would you like to give? 10, 12, or 15?"))
split = int(input("How many people to split the bill?"))

tip_amount = tip / 100 * bill
total_bill = tip_amount + bill
each_person = total_bill / split

# total = (((tip / 100) * bill) + bill)/split
print(f"Each person should pay ${each_person}")