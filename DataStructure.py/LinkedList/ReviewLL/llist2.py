class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(data = new_data)

        new_node.next = self.head
        new_node.prev = None

        if self.head != None:
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return
        
        new_node = Node(data=new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    # can do both Before and After
    def insertByIndex(self, index, new_data):
        new_node = Node(data = new_data)

        if self.head is None:
            if index == 0:
                self.head = new_node
                return
            else:
                print("Data cannot be added")
                return
        
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
            return

        temp = self.head
        for i in range(index-1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            print("Data cannot be added")
            return
        else:
            pass
            # print("index =", index, "and data =", new_data)

        if temp.next is None:
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None
        else:
            new_node.next = temp.next
            temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp        


    def append(self, new_data):
        new_node = Node(data=new_data)

        temp = self.head
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        
        while temp.next != None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def removeByData(self, data):
        temp = self.head
        count = 0
        while temp != None:
            if temp.data == data:
                if temp.next is None:
                    if temp.prev != None:
                        temp.prev.next = None
                        temp = None
                    else:
                        self.head = None
                    return count
                else:
                    if temp == self.head:
                        self.head = temp.next
                        temp.next.prev = None
                        return count
                    else:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                        return count
            else:
                temp = temp.next
        
        if temp is None:
            print("Not Found!")
            return 'x'

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def __str__(self):
        if self.head is None:
            print("")
            return
        
        temp = self.head
        while temp != None:
            if temp.next == None:
                print(temp.data)
            else:
                print(temp.data, end='->')
            temp = temp.next

    def str_reverse(self):
        if self.head is None:
            print("")
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next 
        # Now temp is tail

        while temp != None:
            if temp.prev == None:
                print(temp.data)
            else:
                print(temp.data, end='->')
            temp = temp.prev

    def isEmpty(self):
        temp = self.head
        count = 0
        while temp != None:
            count = count+1
            temp = temp.next
        return count == 0


inp = input("Enter Input : ").split(',')

ll = DoublyLinkedList()

for i in range(0, len(inp), 1):
    if inp[i][0] is 'A':
        if inp[i][1] is 'b':
            ll.push(inp[i][3:])
            print("linked list : ",end='')
            ll.__str__()
            print("reverse : ",end='')
            ll.str_reverse()
        else:
            ll.append(inp[i][2:])
            print("linked list : ",end='')
            ll.__str__()
            print("reverse : ",end='')
            ll.str_reverse()
    elif inp[i][0] is 'I':
        tempIndex = ""
        count = 1
        for j in range(2, len(inp[i]), 1):
            count = count+1
            if inp[i][j] == ':':
                count = count+1
                break
            tempIndex = tempIndex + inp[i][j]
        tempIndex = int(tempIndex)
        
        temp = ""
        for j in range(count+1, len(inp[i]), 1):
            temp = temp+inp[i][j]

        ll.insertByIndex(tempIndex, temp)
        print("linked list : ",end='')
        ll.__str__()
        print("reverse : ",end='')
        ll.str_reverse()
        tempIndex = ""
        temp = ""
    
    elif inp[i][0] is 'R':
        ll.removeByData(inp[2:])