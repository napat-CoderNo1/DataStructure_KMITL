class Stack:
    def __init__(self, list=None): # With Defualt Argument
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def push(self, new_data):
        self.items.append(new_data)

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        return self.items.pop()
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def __str__(self):
        pass

print("******** Parking Lot ********")
#  5     1,2,3 arrive   1
maxcar,carInsoi,oper,numofcar = input("Enter max of car,car in soi,operation : ").split()

maxcar,numofcar = int(maxcar),int(numofcar)

MrGorPark = Stack()
MrKhorPark = Stack()

for i in carInsoi:
    if i != ',' and i!= '0':
        MrGorPark.push(int(i))

if oper == "arrive":
    if MrGorPark.size() != maxcar:
        if numofcar not in MrGorPark.items:
            print("car", numofcar, "arrive! : Add Car", numofcar)
            MrGorPark.push(numofcar)
        else:
            print("car", numofcar, "already in soi")
    else:
        print("car", numofcar,"cannot arrive : Soi Full")
    print(MrGorPark.items)
elif oper == "depart":
    if MrGorPark.isEmpty():
        print("car", numofcar, "cannot depart : Soi Empty")
        print(MrGorPark.items)
    else:
        if numofcar in MrGorPark.items:
            while MrGorPark.peek() != numofcar:
                temp = MrGorPark.pop()
                MrKhorPark.push(temp)
            else:
                MrGorPark.pop()
                while MrKhorPark.size() > 0:
                    temp = MrKhorPark.pop()
                    MrGorPark.push(temp)
            print("car", numofcar, "depart ! : Car", numofcar, "was remove")
            print(MrGorPark.items)
        else:
            print("car", numofcar, "cannot depart : Dont Have Car", numofcar)
            print(MrGorPark.items)