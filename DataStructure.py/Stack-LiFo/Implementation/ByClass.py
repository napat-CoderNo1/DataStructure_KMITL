class Stack:

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        # self.size = len(self.items)

    def push(self, i):
        self.items.append(i)
        # self.size += 1

    def pop(self):
        # self.size -= 1
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        # return self.items = []
        return len(self.items) == 0

    def isFull(self):
        pass

    def size(self):
        return len(self.items)

    def __str__(self):
        s = 'stack of '+str(self.size())+' items : '
        for i in self.items:
            s += str(i)+' '
        return s 
        

s = Stack()
print(s.items)
print(s.size())

s1 = Stack(['A','B','C'])
print(s1.items)
print(s1.size())

print(s1.pop())
print(s1.items)
print(s1.size())
print(s1.peek())
print(s1.isEmpty())
print(s1.size())
print(s1.__str__())
# print(s1.size)