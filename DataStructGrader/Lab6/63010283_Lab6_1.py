def factorial(number):
    if number == 0:
        return 1
    
    if number == 1:
        return number
    else:
        return number * factorial(number-1)

inp = input("Enter Number : ")
x = factorial(int(inp))
print(str(inp)+"! =", x)