def bubble(l):
    for last in range(len(l)-1, -1, -1):
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            break

def selection(l):
    for last in range(len(l)-1, -1, -1):
        biggest = l[0]
        biggest_index = 0
        for i in range(1, last+1, 1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_index = i
        l[last], l[biggest_index] = l[biggest_index], l[last]

def insertion(l):
    for i in range(1, len(l), 1):
        iEle = l[i]
        for j in range(i, -1, -1):
            if iEle<l[j-1] and j>0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break


l = [4,1,6,5,3,2]
insertion(l)
# selection(l)
# bubble(l)
print(l)