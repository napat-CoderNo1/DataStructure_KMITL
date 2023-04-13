def bubble(l):
    for last in range(len(l)-1, -1, -1):
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            break

def bubble2(l):
    for last in range(len(l)-1, -1, -1):
        swaped = False
        for i in range(last):
            if len(l[i]) > len(l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            break

def check1(i, l=[]):
    if i == 0:
        return
    elif len(l[i]) != len(l[i-1]):
        return 
    elif len(l[i]) == len(l[i-1]):
        for j in range(len(l[i])):
            if l[i][j] == l[i-1][j]:
                pass
            elif l[i][j] < l[i-1][j]:
                    l[i], l[i-1] = l[i-1], l[i]
                    return check1(i-1, l)
            elif l[i][j] > l[i-1][j]:
                return 


def bubble3(l):
    for i in range(len(l)-1):
        if len(l[i]) == len(l[i+1]):
            for j in range(len(l[i])):
                if l[i][j] > l[i+1][j]:
                    l[i], l[i+1] = l[i+1], l[i]
                    break
        check1(i, l)


# return subset of list
def subset(l):
    if l == []:
        return [[]]
    
    x = subset(l[1:])

    return x + [[l[0]] + y for y in x]


inp = input("Enter Input : ").split("/")
# print(inp)
# print(inp[0])
inp[1] = inp[1].split()

for i in range(len(inp[1])):
    inp[1][i] = int(inp[1][i])
# print(inp[1])

# print(subset(inp[1]))

lis = []

check = False

for i in subset(inp[1]):
    if sum(i) == int(inp[0]):
        lis.append(i)
        check = True

if check == True:
    bubble2(lis)

    for i in lis:
        bubble(i)

    # for i in range(len(lis)):
    #     print(lis[i])

    # print("-----------------------")

    bubble3(lis)
    for i in range(len(lis)):
        print(lis[i])
else:
    print("No Subset")
