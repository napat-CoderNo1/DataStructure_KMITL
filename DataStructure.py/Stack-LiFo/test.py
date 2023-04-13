class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, new_data):
        self.items.append(new_data)
        self.size = self.size+1

    def pop(self):
        self.size = self.size-1
        return self.items.pop()

    def peek(self):
        pass

    def isEmpty(self):
        pass

    def isFull(self):
        pass

    def Size(self):
        pass


s = Stack()
s.push('b')
s.push('c')
print(s.pop())

'''s.push('a')
s.push('b')
s.push('c')
print(s.size)
s.pop()
print(s.items)
print(s.size)'''