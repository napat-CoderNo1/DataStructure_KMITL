class Stack:
    def __init__(self):
        self.items = []
        self.size = 0 # ไม่ต้องมีก็ได้เพราะมี method size() เเล้ว

    def push(self, new_data):
        self.items.append(new_data)
        self.size +=1 # ไม่ต้องมีก็ได้เพราะมี method size() เเล้ว

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        self.size -= 1 # ไม่ต้องมีก็ได้เพราะมี method size() เเล้ว
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


s = Stack()
print(s.items)
s.push('A')
print(s.items)
print(s.isEmpty())
print(s.pop())
print(s.items)
print(s.isEmpty())