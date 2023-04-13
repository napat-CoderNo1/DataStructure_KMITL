class Queue1:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, new_Data):
        self.items.append(new_Data)

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Popping from an empty queue")
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def isFull(self):
        pass

    def size(self):
        return len(self.items)

    def front(self):
        if self.isEmpty():
            raise Exception("empty queue")
        return self.items[0]

    def tail(self):
        if self.isEmpty():
            raise Exception("empty queue")
        return self.items[-1]

mainRow = Queue1()
cashier1 = Queue1()
cashier2 = Queue1()

people = input("Enter people : ")
for i in people:
    mainRow.enQueue(i)

i = 0
timetemp = 0
while True:
    i = i+1
    temp1 = mainRow.deQueue()
    
    if i>3 and (i-1) % 3 ==0:
        cashier1.deQueue()
    
    if i>timetemp and i%2==0 and cashier2.size()>0:
        cashier2.deQueue()

    if cashier1.size() == 5:
        cashier2.enQueue(temp1)
    else:
        cashier1.enQueue(temp1)
    
    if cashier2.size() == 1:
        timetemp = i

    print(i,mainRow.items,cashier1.items,cashier2.items)

    if mainRow.size() == 0:
        break