def table(number):
    for i in range(1, 11):
        print(f"{number}x{i} = {number*i}")

input1 = int(input("Insert a number: "))
table(input1)

"""
3x1 = 3
3x2 = 6
3x3 = 9
.
.
.
.
.
3x10 = 30
"""