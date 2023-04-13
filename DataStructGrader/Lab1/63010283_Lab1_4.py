def f4(n):
    for i in range(0, n, 1):
        print("."*(n-1-i), end='')
        print("*", end='')
        if i != 0:
            print("+"*(((i-1)*2)+1), end='')
            print("*", end='')
        
        print("."*(n-1-i), end='')
        print("."*(n-2-i), end='')
        if i != n-1:
            print("*", end='')
        if i != 0:
            print("+"*(((i-1)*2)+1), end='')
            print("*", end='')
        print("."*(n-1-i), end='')
        print("")


def tail(n):
    for j in range((n*2)-2, 0, -1):
        print("."*(((n*2)-1)-j), end='')
        print("*", end='')
        print("+"*((j*2)-3), end='')
        if j != 1:
            print("*", end='')
        print("."*(((n*2)-1)-j))


def f6(n):
    f4(n)
    tail(n)


print("*** Fun with Drawing ***")
number = int(input("Enter input : "))
f6(number)
