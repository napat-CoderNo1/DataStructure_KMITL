class Node:
    def __init__(self, data, id):
        self.data = data
        self.id = id
    
    def __str__(self):
        return str(self.data)

inp = input("Enter Input : ").split("/")

inp[0] = int(inp[0])
inp[1] = inp[1].split()

lis = []

for i in range(inp[0]):
    lis.append(Node(0, i))

for i in range(len(inp[1])):
    lis[0].data = lis[0].data+int(inp[1][i])
    print("Customer "+ str(i+1) + " Booking Van ", end='')
    print(lis[0].id+1, end=' ')
    print("| " + inp[1][i] + " day(s)")
    lis.sort(key=lambda x: x.data, reverse=False)
    for i in range(inp[0]-1):
        if lis[i].data == lis[i+1].data:
            if lis[i].id > lis[i+1].id:
                lis[i], lis[i+1] = lis[i+1], lis[i]
    # if lis[0].data == lis[1].data:
    #     if lis[0].id > lis[1].id:
    #         lis[0], lis[1] = lis[1], lis[0]
    # elif lis[1].data == lis[2].data:
    #     if lis[1].id > lis[2].id:
    #         lis[1], lis[2] = lis[2], lis[1]


# for i in range(3):
#     print(lis[i].data)

# lis[0].data = lis[0].data+3

# for i in range(3):
#     print(lis[i].data)

# lis.sort(key=lambda x: x.data, reverse=False)

# for i in range(3):
#     print(lis[i].data)