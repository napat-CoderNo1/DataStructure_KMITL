'''
    *
   **
  ***
 ****
*****
'''
def f0(n):
    for i in range(0, n, 1):
        print(" "*(n-1-i), end='')
        print("."*(i+1))

'''
*
**
***
****
*****
'''
def f1(n):
    for i in range(0, n, 1):
        for j in range(0, i+1, 1):
            print(".", end='')
        print("")


'''
*****
****
***
**
*
'''
def f2(n):
    for i in range(n, 0, -1):
        for j in range(0, i, 1):
            print(".", end='')
        print("")


'''
*****
 ****
  ***
   **
    *
'''
def f3(n):
    for i in range(0, n, 1):
        print(" "*i, end='')
        print("."*(n-i), end='')
        print("")


'''
     *
    ***
   *****
  *******
 *********
'''

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

'''
*********
 *******
  *****
   ***
    *
'''
def test(n):
    for i in range(0, n, 1):
        print(" "*(i), end='')
        print("*"*(((n-i)*2)-1), end='')
        print(" "*(i))


def mid(n):
    print(".*",end='')
    print("+"*((n*4)-7),end='')
    print("*.",end='')


def tail(n):
    for j in range((n*2)-2, 0, -1):
        print("."*(((n*2)-1)-j), end='')
        print("*", end='')
        print("+"*((j*2)-3), end='')
        if j != 1:
            print("*", end='')
        print("."*(((n*2)-1)-j))

tail(2)
print("\n")
tail(5)
print("\n")
tail(7)