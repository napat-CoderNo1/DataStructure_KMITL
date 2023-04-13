def bubble(l):
    for last in range(len(l)-1, -1, -1):
        swaped = False
        for i in range(last):
            if ord(l[i]) > ord(l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            break

inp = input("Enter Input : ").split()

# inp = ["932c", "832u32", "2344b"]

dic = {}

number = ["0","1","2","3","4","5","6","7","8","9"]

for i in range(len(inp)):
    for j in inp[i]:
        if j not in number:
            dic[j] = inp[i]

# print(dic)

lis = []

for i in dic.keys():
    lis.append(i)

bubble(lis)

for i in lis:
    print(dic[i], end=' ')