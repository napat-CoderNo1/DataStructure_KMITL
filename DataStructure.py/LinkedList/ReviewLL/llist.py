class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

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

    def append(self, new_data):

        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next != None:
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
    
    def returnTail(self):

        if self.head is None:
            return

        if self.head.next is None:
            return self.head.data
        
        temp = self.head

        while temp.next != None:
            temp = temp.next
        
        return temp.data

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

ll = LinkedList()

paren = {'[':']', '(':')'}

open = ['[', '(']

close = [']', ')']

inp = input("Enter Input : ")

check = False

for i in range(0, len(inp), 1):
    if i == 0:
        if inp[i] in close:
            print("Parentheses : Unmatched ! ! !")
            check = True
            break
        elif inp[i] in open:
            ll.append(inp[i])
    else:
        if inp[i] in open:
            ll.append(inp[i])
        elif inp[i] in close:
            if ll.size() != 0:
                if paren[ll.returnTail()] == inp[i]:
                    ll.deleteTail()
                else:
                    print("Parentheses : Unmatched ! ! !")
                    check = True
                    break
            else:
                print("Parentheses : Unmatched ! ! !")
                check = True
                break

if ll.size() == 0 and check == False:
    print("Parentheses : Matched ! ! !")
elif check == False:
    print("Parentheses : Unmatched ! ! !")