num = int(input("Enter Input : "))

for i in range(num+1, 0, -1):
    
    for j in range(0, i, 1):
        print(".", end='')
    
    print("#"*((num+1)-j), end='')

    print("+", end='')

    if i == num+1:
        print("+"*(num+1), end='')
    else:
        print("#"*(num), end='')
        print("+", end='')

    print("")


print("#"*(num+2), end='')
print("+"*(num+2))
print("#"*(num+2), end='')
print("+"*(num+2))


for i in range(num, 0, -1):
    print("#", end='')
    print("+"*num, end='')
    print("#", end='')
    print("+"*(i+1), end='')
    print("."*(num+1-i))

print("#"*(num+2), end="")
print("+", end="")
print("."*(num+1))