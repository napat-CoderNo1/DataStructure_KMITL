myList = input("Enter Your List : ").split(" ")

if len(myList) <3:
    print("Array Input Length Must More Than", len(myList))
else:
    tempList2 = []

    for i in range(len(myList)):
        myList[i] = int(myList[i])

    for i in range(0, len(myList)-2, 1):
        for j in range(i+1, len(myList)-1, 1):
            for k in range(j+1, len(myList), 1):
                if myList[i]+myList[j]+myList[k] == 0: 
                    if [myList[i], myList[j], myList[k]] in tempList2:
                        pass
                    else:
                        tempList2.append([myList[i], myList[j], myList[k]])               

    print(tempList2)