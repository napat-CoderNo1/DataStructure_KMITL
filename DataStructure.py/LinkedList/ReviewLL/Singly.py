class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print("")
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAfterByIndex(self, index, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head

        if index == 0:
            new_node.next = temp.next
            temp.next = new_node
            return
        
        for i in range(index):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            return

        new_node.next = temp.next
        temp.next = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def deleteByKey(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next # None
                temp = None
                return
        
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return
        
        prev.next = temp.next
        temp = None

    def deleteByIndex(self, index):
        if self.head == None:
            return

        temp = self.head
        
        if index == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(index-1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def deleteTail(self):

        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        
        temp.next = None

    def popFirstNode(self):
        temp = self.head
        self.head = temp.next
        x = temp
        temp = None
        return x

    def popTail(self):

        if self.head is None:
            return

        if self.head.next is None:
            return self.head.data
        
        temp = self.head

        while temp.next != None:
            temp = temp.next
        
        return temp.data

    def size(self):
        if self.head is None:
            return 0

        if self.head.next is None:
            return 1

        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        
        return count