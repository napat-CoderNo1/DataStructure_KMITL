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

    def __str__(self):
        return " ".join(str(x) for x in self.items)

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

    def popFirst(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return " ".join([str(x) for x in self.items])

inp = input("Enter Input (Normal, Mirror) : ").split(" ")

s = Stack()
ss = Stack()
boom = Queue()
count = 0

sNormal = Stack()
ssNormal = Stack()
bNormal = Queue()

x = inp[1]
x = x[::-1]
for i in range(0 , len(x), 1):
    if s.isEmpty():
        s.push(x[i])
        count = 1  
    else:
        if x[i] == s.peek():
            s.push(x[i])
            count = count+1
            if count == 3:
                s.pop()
                s.pop()
                boom.enQueue(s.pop())
                while True:
                    if s.isEmpty():
                        break
                    ss.push(s.popFirst())
                while True:
                    if ss.isEmpty():
                        break
                    if s.isEmpty():
                        s.push(ss.popFirst())
                        count = 1
                    else:
                        temp = ss.popFirst()
                        if temp == s.peek():
                            s.push(temp)
                            count = count+1
                        else:
                            s.push(temp)
                            count = 1
        else:
            s.push(x[i])
            count = 1

mirrorBoomCount = boom.size()
countInterrup = 0
count = 0
y = inp[0]
for i in range(0, len(y), 1):
    if sNormal.isEmpty():
        sNormal.push(y[i])
        count = 1
    else:
        if y[i] == sNormal.peek():
            sNormal.push(y[i])
            count = count+1
            if count == 3:
                if boom.isEmpty():
                    sNormal.pop()
                    sNormal.pop()
                    bNormal.enQueue(sNormal.pop())
                    while True:
                        if sNormal.isEmpty():
                            break
                        ssNormal.push(sNormal.popFirst())
                    while True:
                        if ssNormal.isEmpty():
                            break
                        if sNormal.isEmpty():
                            sNormal.push(ssNormal.popFirst())
                            count = 1
                        else:
                            temp = ssNormal.popFirst()
                            if temp == sNormal.peek():
                                sNormal.push(temp)
                                count = count+1
                            else:
                                sNormal.push(temp)
                                count = 1
                else:
                    item = boom.deQueue()
                    temp = sNormal.pop()
                    if item == temp:
                        countInterrup = countInterrup+1
                        sNormal.pop()
                        sNormal.pop()
                        sNormal.push(temp)
                        count = 1
                    else:
                        sNormal.push(item)
                        sNormal.push(temp)
                        count = 1
                    
        else:
            sNormal.push(y[i])
            count = 1


print("NORMAL :")
print(sNormal.size())
# print("sNormal.items = ", sNormal.items)
if sNormal.size() == 0:
    print("Empty", end='')
else:
    for i in range(len(sNormal.items)-1, -1, -1):
        print(sNormal.items[i], end='')
print("\n"+str(bNormal.size()),end=' ')        
print("Explosive(s) ! ! ! (NORMAL)")
if countInterrup > 0:
    print("Failed Interrupted", countInterrup, "Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(s.size())
if s.size() == 0:
    print("ytpmE", end='')
else:
    for i in range(len(s.items)-1, -1, -1):
        print(s.items[i], end='')
print("\n(RORRIM) ! ! ! (s)evisolpxE", mirrorBoomCount)
