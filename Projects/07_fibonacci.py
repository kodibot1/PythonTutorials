fib_input = int(input("How many fib no.s you need? "))

def fib_gen(number):
    a = 0
    b = 1
    if number == 1:
        print(a)
    elif number == 2:
        print(a, b)
    else:
        print(a, b, end = " ")
        for i in range(number - 2):
            c = a+b
            a=b
            b=c
            print(c, end = " ")

fib_gen(fib_input)
