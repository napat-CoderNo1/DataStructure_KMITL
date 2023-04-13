def ascending(inp):
    check = True
    for i in range(0, len(inp), 1):
        for j in range(i+1, len(inp), 1):
            if inp[i] > inp[j]:
                check = False
                break
    return check

def descending(inp):
    check = True
    for i in range(0, len(inp), 1):
        for j in range(i+1, len(inp), 1):
            if inp[i] < inp[j]:
                check = False
                break
    return check

def repetitive(inp):
    check = False
    temp = []
    for i in inp:
        if i not in temp:
            temp.append(i)
        else:
            check = True
            break
    return check

# เลขเดียวกันทั้ง list
def sameNumber(lis):
    check = True
    temp = lis[0]
    for i in lis:
        if i == temp:
            pass
        else:
            check = False
            break
    return check


inp = input("Enter Input : ")

lis = []

for i in inp:
    lis.append(int(i))


if sameNumber(lis) == True:
    print("Repdrome")
elif ascending(lis) == True:
    if repetitive(lis) == True:
        print("Plaindrome")
    else:
        print("Metadrome")
elif descending(lis) == True:
    if repetitive(lis) == True:
        print("Nialpdrome")
    else:
        print("Katadrome")
else:
    print("Nondrome")