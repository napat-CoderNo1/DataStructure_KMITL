class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

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

    def insertAfter(self, prev, data):
        
        if prev is None:
            print("prev node must be in List")
            return
        
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def insertAfterByPo(self, position, data):

        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head

        if position == 0:
            new_node.next = temp.next
            temp.next = new_node
            return

        for i in range(position):
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

    def deletionNode(self, key):
        temp = self.head
        
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        
        temp = None

    def deleteByPosition(self, position):
        
        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(position-1):
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
