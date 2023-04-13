print("*** Mod Position ***")
emptyList = []
x, y = input("Enter Input : ").split(",")
y = int(y)

for i in range(0, len(x), 1):
    if (i+1)%y == 0:
        emptyList.append(x[i])

print(emptyList)