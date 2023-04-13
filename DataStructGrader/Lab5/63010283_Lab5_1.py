class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    

    #size
    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count+1
            temp = temp.next
        return count

    
    # Traversal
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print("")
    

    def returnTail(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            return self.head.data

        temp = self.head
        while temp.next != None:
            temp = temp.next
        
        return temp.data
    
    
    # insertion
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    
    def insertAfter(self, prev_node, data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    

    def insertAfterByPo(self, position, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        temp = self.head

        if position == 0:
            new_node.next = temp.next
            temp.next = new_node
            return

        for i in range(0, position, 1):
            temp = temp.next
            if temp == None:
                break
        
        if temp == None:
            return
        
        new_node.next = temp.next
        temp.next = new_node


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = new_node

    
    # deletion
    def deleteNode(self, key):
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
        
        if temp == None:
            print("The given key must inLinkedList.")
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

        for i in range(0, position-1, 1):
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

    def deleteLastNode(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            return
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None     


llist = LinkedList()

paren = {'(':')', '[':']'}
open = ['(', '[']
close = [')', ']']

m = False

x = input("Enter Input : ")

for i in range(0, len(x), 1):
    if llist.head is None:
        if x[i] in close:
            print("Parentheses : Unmatched ! ! !")
            m = True
            break
        elif x[i] in open:
            llist.head = Node(x[i])
    else:
        if x[i] in open:
            llist.append(x[i])
        elif x[i] in close:
            if x[i] == paren[llist.returnTail()]:
                llist.deleteLastNode()
            else:
                print("Parentheses : Unmatched ! ! !")
                m = True
                break

if llist.size() == 0 and m == False:
    print("Parentheses : Matched ! ! !")
else:
    if m == False:
        print("Parentheses : Unmatched ! ! !")
