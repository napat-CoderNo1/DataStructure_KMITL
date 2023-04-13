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

inp = input("Enter Infix : ")

S = Stack()
# index   0    1    2    3    4    5    6
items = ['-', '+', '*', '/', '(', ')', '^']
plusminus = ['+', '-']
muldiv = ['*', '/']

print("Postfix : ", end='')

for i in range(0, len(inp), 1):
    if inp[i] not in items:
        print(inp[i], end='')
    else:
        if S.isEmpty():
            S.push(inp[i])
        else:
            if inp[i] == ')':
                while S.peek() != '(':
                    print(S.pop(), end='')
                else:
                    S.pop()
            if inp[i] == '(':
                S.push(inp[i])
            if inp[i] == '^':
                S.push(inp[i])
            if inp[i] in muldiv:
                while S.peek() in muldiv or S.peek() == '^':
                    print(S.pop(), end='')
                    if S.isEmpty():
                        S.push(inp[i])
                        break
                else:
                    S.push(inp[i])
            if inp[i] in plusminus:
                while S.peek() in muldiv or S.peek() in plusminus or S.peek() == '^':
                    print(S.pop(), end='')
                    if S.isEmpty():
                        S.push(inp[i])
                        break
                else:
                    S.push(inp[i])
                

while not S.isEmpty():

    print(S.pop(), end='')

print()