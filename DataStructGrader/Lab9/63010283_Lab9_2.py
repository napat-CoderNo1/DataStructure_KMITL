# return int ที่มากที่สุดใน list
def Max(list):
    if len(list) == 1:
        return int(list[0])
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

# ใส่ i เริ่มที่ 0 เสมอ return index ของตัวที่เราหา
def findIndex(number, i, list=[]):
    if list[i] == number:
        return int(i)
    else:
        return findIndex(number, i+1, list)

def recursiveSelection(inp, Index, temp, count):
    if Index == 0:
        print(inp)
        return 
    maxNum = Max(temp)
    # print(maxNum)
    rightOfTemp = temp[-1]
    # print(rightOfTemp)
    if maxNum != rightOfTemp:
        print("swap", rightOfTemp, "<->", maxNum, ":", end=' ')
    x = findIndex(maxNum, 0, inp)
    # print("x=",x)
    y = findIndex(rightOfTemp, 0, inp)
    # print("y = ", y)
    inp[x], inp[y] = inp[y], inp[x]
    if maxNum != rightOfTemp:
        print(inp)
    temp = inp
    count = count+1
    return recursiveSelection(inp, Index-1,temp[:-count], count)

    

inp = [int(i) for i in input("Enter Input : ").split()]

recursiveSelection(inp, len(inp)-1, inp, 0)