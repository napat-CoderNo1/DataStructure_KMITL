class StackCalc:
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

    def run(self, instructions):
        
        for i in range(0, len(instructions), 1):
            
            number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            test = True

            if instructions[i] == '+':
                temp1 = self.items.pop()
                temp1 = int(temp1)
                temp2 = self.items.pop()
                temp2 = int(temp2)
                temp3 = temp1 + temp2
                self.items.append(temp3)
            elif instructions[i] == '-':
                temp1 = self.items.pop()
                temp1 = int(temp1)
                temp2 = self.items.pop()
                temp2 = int(temp2)
                temp3 = temp1 - temp2
                self.items.append(temp3)
            elif instructions[i] == '*':
                temp1 = self.items.pop()
                temp1 = int(temp1)
                temp2 = self.items.pop()
                temp2 = int(temp2)
                temp3 = temp1 * temp2
                self.items.append(temp3)
            elif instructions[i] == '/':
                temp1 = self.items.pop()
                temp1 = int(temp1)
                temp2 = self.items.pop()
                temp2 = int(temp2)
                temp3 = temp1 / temp2
                temp3 = int(temp3)
                self.items.append(temp3)
            elif instructions[i] == 'DUP':
                temp1 = self.items.pop()
                self.items.append(temp1)
                self.items.append(temp1)
            elif instructions[i] == 'POP':
                self.items.pop()
            elif instructions[i] == 'PSH':
                pass
            else:
                for j in instructions[i]:
                    if j not in number:
                        test = False
                if test == False:
                    return 'x'
                else:
                    self.items.append(instructions[i])
                        
                
    
    def getValue(self):
        if len(self.items) != 0:
            return self.items[-1]
        else: 
            return 0


print("* Stack Calculator *")
arg = input("Enter arguments : ").split(" ")
machine = StackCalc()
machine.run(arg)
if machine.run(arg) != 'x':
    print(machine.getValue())
else:
    print("Invalid instruction:", arg[0])