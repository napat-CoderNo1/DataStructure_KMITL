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
    
    def deleteNode(self, key):
        
        temp = self.head
        
        if temp is not None:
            if self.head.data == key:
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


'''Delete By Position'''
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)
 
print("Created Linked List: ")
llist.printList()
llist.deleteByPosition(4)
print("\nLinked List after Deletion at position 4: ")
llist.printList()


''' Delete By Given key
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
 
print ("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print ("\nLinked List after Deletion of 1:")
llist.printList()'''