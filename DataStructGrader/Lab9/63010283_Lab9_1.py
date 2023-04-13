inp = [int(i) for i in input("Enter Input : ").split()]

check = True

for i in range(0, len(inp), 1):
    for j in range(i+1, len(inp), 1):
        if inp[i] > inp[j]:
            check = False
            break

if check == True:
    print("Yes")
else:
    print("No") 