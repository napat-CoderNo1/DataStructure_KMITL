# print(ord('A'))
# print(chr(65))

def Max(list):
    if len(list) == 1:
        return int(list[0])
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

def findIndex(number, i, list=[]):
    if list[i] == number:
        return int(i)
    else:
        return findIndex(number, i+1, list)

def ascending(inp):
    check = True
    for i in range(0, len(inp), 1):
        for j in range(i+1, len(inp), 1):
            if inp[i] > inp[j]:
                check = False
                break
    return check


# print(findIndex(5, 0, [11,2,5,7,499]))
# print(Max([11,2,5,7,499]))

print(ascending([5,4,3,2,1]))