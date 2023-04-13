def search(sortedL1, l2):
    # print(l2)
    for i in l2:
        check = False
        for j in sortedL1:
            if j>i:
                check = True
                print(j)
                break
        if check == False:
            print("No First Greater Value")


inp = [i.split() for i in input("Enter Input : ").split("/")]
# inp = input("Enter Input : ").split("/")

for i in range(len(inp[0])):
    inp[0][i] = int(inp[0][i])

for i in range(len(inp[1])):
    inp[1][i] = int(inp[1][i])

inp[0].sort()

# print(inp[0])
# print(inp[1])

search(inp[0], inp[1])