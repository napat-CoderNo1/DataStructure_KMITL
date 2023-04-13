from classStack2 import Stack

def match(open,close):
    return (open == '(' and close == ')') or (open == '[' and close == ']') or (open == '{' and close == '}')

def parenMatching(str):
    s = Stack()
    i = 0
    error = 0

    while i < len(str) and error == 0:
        c = str[i]
        if c in '{[(':
            s.push(c)
        else:
            if c in '}])':
                if s.size() > 0:
                    if not match(s.pop(),c):
                        error = 1 # error format1 => Unmatch open-close
                else: # empty stack
                    error = 2 # error format2 => close paren excess
        i+=1

    if s.size() > 0:
        error = 3
    
    return error,c,i,s

v = input("Enter expression : ")

print(parenMatching(v))
