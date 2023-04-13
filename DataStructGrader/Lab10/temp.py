from copy import deepcopy

def box(weigth, lis, inp):
    tLis = deepcopy(lis)
    tInp = deepcopy(inp)
    # tLis = [tLis.append(i) for i in lis]
    # tInp = [tInp.append(i) for i in inp]
    # print(tLis)
    # print(tInp)
    
    count = 0
    for i in range(len(tLis)):
        
        for j in tInp:
            tLis[i].append(j)
            if sum(tLis[i]) > weigth:
                tLis[i].pop()
            else:
                count += 1
        
        for k in range(count):
            tInp.pop(0)
        count = 0
    
    if len(tInp) == 0:
        return weigth
    else:
        return box(weigth+1, lis, inp)


inp = [i.split() for i in input("Enter Input : ").split("/")]

for i in range(len(inp[0])):
    inp[0][i] = int(inp[0][i])

for i in range(len(inp[1])):
    inp[1][i] = int(inp[1][i])

weigth = max(inp[0])

lis = []

for i in range(inp[1][0]):
    lis.append([])

print(box(weigth, lis, inp[0]))
# box(weigth, lis, inp[0])

# [[] [] []]