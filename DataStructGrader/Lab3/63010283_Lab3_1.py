stack = []

message = input("Enter Input : ").split(",")

for i in message:
    x = i
    
    if x[0] == 'A':
        stack.append(x[2:])
        print("Add =",x[2:],"and","Size =",len(stack))
    
    if x[0] == 'P':
        if len(stack) == 0:
            print("-1")
        else:
            print("Pop =",stack[len(stack)-1],"and Index =",len(stack)-1)
            stack.pop()

if len(stack) == 0:
    print("Value in Stack = Empty")
else:
    print("Value in Stack =",end=' ')
    for i in stack:
        print(i,end=' ')