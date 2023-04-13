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
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev, data):
        if prev is None:
            print("prev must be in LinkedList")
            return
        
        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def insertAfterByPosition(self, position,data):
        
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
    
    def append(self ,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    

llist = LinkedList()

# Insert 6.  So linked list becomes 6->None
llist.append(6)

# Insert 7 at the beginning. So linked list becomes 7->6->None
llist.push(7)

# Insert 1 at the beginning. So linked list becomes 1->7->6->None
llist.push(1)

# Insert 4 at the end. So linked list becomes 1->7->6->4->None
llist.append(4)

# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
llist.insertAfter(llist.head.next, 8)

print('Created linked list is:')
llist.printList()