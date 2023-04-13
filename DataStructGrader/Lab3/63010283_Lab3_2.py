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

open = ['[','{','(']
close = [']','}',')']
message = {']':'[', '}':'{', ')':'('}
finish = False

s = Stack()

p = input("Enter expresion : ")

for i in range(0,len(p),1):
    if i == 0 and p[i] in close:
        print(p,"close paren excess")
        finish = True
        break
    elif i!=0 and s.size() == 0:
        if p[i] in close:
            print(p,"close paren excess")
            finish = True
            break
        elif p[i] in open:
            s.push(p[i])
    elif p[i] in open:
        s.push(p[i])
    elif p[i] in close:
        if message[p[i]] == s.peek() :
            s.pop()
        elif message[p[i]] != s.peek():
            print(p,"Unmatch open-close")
            finish = True
            break

if finish == False:
    if s.isEmpty():
        print(p,"MATCH")
    elif s.peek() in open:
        print(p,"open paren excess  ",s.size(),":",end=' ')
        for i in range(s.size()):
            print(s.items[i],end='')
    elif s.peek() in close:
        print(p,"close paren excess")