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
        pass

inp = input("Enter Input (Normal, Mirror) : ").split(" ")

s = Stack()
ss = Stack()
boom = Queue()
count = 0

s2 = Stack()
ss2 = Stack()
boom2 = Queue()
count2 = 0

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

print(boom.items)

y = inp[0]

for i in range(0 , len(y), 1):
    if s2.isEmpty():
        s2.push(y[i])
        count2 = 1 
    else:
        if y[i] == s2.peek():
            s2.push(y[i])
            count2 = count2+1
            if count2 == 3:
                if boom.isEmpty():
                    s2.pop()
                    s2.pop()
                    boom2.enQueue(s2.pop())
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
                    item = boom.deQueue()
                    if item == s2.peek():
                        temp2 = s2.pop()
                        s2.pop()
                        s2.pop()
                        s2.push(temp2)
                        while True:
                            if s2.isEmpty():
                                break
                            ss2.push(s2.popFirst())
                        while True:
                            if ss2.isEmpty():
                                break
                            if s2.isEmpty():
                                s2.push(ss2.popFirst())
                                count2 = 1
                            else:
                                temp = ss2.popFirst()
                                if temp == s2.peek():
                                    s2.push(temp)
                                    count2 = count2+1
                                else:
                                    s2.push(temp)
                                    count2= 1
                    else:
                        temp2 = s2.pop()
                        s2.push(item)
                        s2.push(temp2)
                        count2 = 1
        else:
            s2.push(y[i])
            count2 = 1

print("NORMAL :")
print(s2.items)