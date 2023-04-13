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