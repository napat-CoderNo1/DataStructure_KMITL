from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enQueue(self, new_data):
        self.items.append(new_data)

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Popping from an empty queue")
        return self.items.popleft()

    def isEmpty(self):
        return len(self.items) == 0

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


q = Queue()

inp = input("Enter Input : ").split(",")

for i in range(0, len(inp), 1):
    for j in range(0, len(inp[i]), 1):
        if j == 0:
            if inp[i][j] == 'E':
                print("Add", inp[i][2:], "index is", q.size())
                temp = int(inp[i][2:])
                q.enQueue(temp)
            elif inp[i][j] == 'D':
                if q.isEmpty():
                    print("-1")
                else:
                    temp = q.deQueue()
                    print("Pop", temp, "size in queue is", q.size())

if q.isEmpty():
    print("Empty")
else:
    print("Number in Queue is :  [", end="")
    for i in range(0, q.size(), 1):
        if i == q.size()-1:
            print("'"+str(q.items[i])+"']", end='')
        else:
            print("'"+str(q.items[i])+"', ", end='')