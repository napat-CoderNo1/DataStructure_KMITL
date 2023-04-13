class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    # Add a node at the front
    def push(self, new_data):
        new_node = Node(data = new_data)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    # Add a node after a given node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return
        
        new_node = Node(data = new_data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    # insert data ใน index ที่กำหนด
    def insertByIndex(self, index, new_data):
        new_node = Node(data = new_data)
        
        if self.head is None:
            if index == 0:
                self.head = new_node
                print("index =", index, "and data =", new_data)
                return
            else:
                print("Data cannot be added")
                return

        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
            print("index =", index, "and data =", new_data)
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
            print("index =", index, "and data =", new_data)
        
        if temp.next is None:
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None
        else:
            new_node.next = temp.next
            temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp        


    # Add a node at the end
    def append(self, new_data):
        new_node = Node(data = new_data)
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
    

    # Add a node before a given node
    def insertBefore(self , given_node, new_data):
        if given_node == None:
            print("the given next node cannot be NULL")
            return
        
        new_node = Node(data = new_data)

        new_node.prev = given_node.prev

        given_node.prev = new_node

        new_node.next = given_node

        if new_node.prev != None:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    # reverse direction
    def  str_reverse(self):
        if self.head is None:
            print("")
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next

        while temp != None:
            if temp.prev is None:
                print(temp.data)
            else:
                print(temp.data, end='->')
            temp = temp.prev
    
    # forward direction
    def __str__(self):
        if self.head is None:
            print("")
            return
        
        temp = self.head
        while temp is not None:
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data, end='->')
            temp = temp.next

    # size
    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count+1
            temp = temp.next
        return count

    def isEmpty(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count+1
            temp = temp.next
        return count == 0

    def remove(self, data):
        count = 0
        temp = self.head
        while temp is not None:
            count = count+1
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


llist = DoublyLinkedList()

x = input("Enter Input : ").split(",")

temp = ""
tempIndex = ""

for i in range(0 , len(x), 1):
    if x[i][0] == ' ':
        x[i] = x[i].strip()
    
    if x[i][0] == 'A':
        if x[i][1] == 'b':
            for j in range(3, len(x[i]), 1):
                temp = temp+x[i][j]
            llist.push(temp)
            temp = ""
            
            print("linked list : ",end='')
            llist.__str__()
            print("reverse : ",end='')
            llist.str_reverse()

        else:
            for j in range(2, len(x[i]), 1):
                temp = temp+x[i][j]
            llist.append(temp)
            temp = ""
            
            print("linked list : ",end='')
            llist.__str__()
            print("reverse : ",end='')
            llist.str_reverse()

    elif x[i][0] == 'I':
        if x[i][2] == '-':
            print("Data cannot be added")
            print("linked list : ", end='')
            llist.__str__()
            print("reverse : ",end='')
            llist.str_reverse()
        else:
            for j in range(2, len(x[i]), 1):
                if x[i][j] == ':':
                    break
                tempIndex = tempIndex+x[i][j]
            tempIndex = int(tempIndex)
            for j in range(4, len(x[i]), 1):
                temp = temp+x[i][j]
            llist.insertByIndex(tempIndex, temp)
            print("linked list : ",end='')
            llist.__str__()
            print("reverse : ",end='')
            llist.str_reverse()
            tempIndex = ""
            temp = ""

    elif x[i][0] == 'R':
        for j in range(2, len(x[i]), 1):
                temp = temp+x[i][j]
        
        tem = llist.remove(temp)
        
        if tem != 'x':
            print("removed :",temp,"from index :", tem-1)
        
        print("linked list : ",end='')
        llist.__str__()
        print("reverse : ",end='')
        llist.str_reverse()
        
        temp = ""

    # elif x[i][0] == ' ':
    #     print("Data cannot be added")
    #     print("linked list : ",end='')
    #     llist.__str__()
    #     print("reverse : ",end='')
    #     llist.str_reverse()
    #     break