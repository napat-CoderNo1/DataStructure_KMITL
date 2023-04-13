def staircase(n, x):
    if n == 0:
        print("Not Draw!")
    elif n > 0:
        if n == 1:
            print("_"*(n-1), end='')
            print("#"*x)
            return
        print("_"*(n-1), end='')
        print("#"*x)
        n = n-1
        x = x+1
        staircase(n,x)
    elif n < 0:
        if n == -1:
            print("_"*(x-1), end='')
            print("#"*abs(n))
            return
        print("_"*(x-1), end='')
        print("#"*abs(n))
        n = n+1
        x = x+1
        staircase(n, x)


n = input("Enter Input : ")
n = int(n)
staircase(n,1)