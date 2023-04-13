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

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def popFirstNode(self):
        temp = self.head
        self.head = temp.next
        x = temp
        temp = None
        return x
    
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

        x = temp.next.data

        temp.next = None
        temp.next = next

        return x
    


def createLL(LL):
    llist = LinkedList()
    for i in LL:
        llist.append(i)
    return llist

def printLL(head):
    temp = head.head
    while temp != None:
        print(temp.data, end=' ')
        temp = temp.next
    print("")

def SIZE(head):
    temp = head.head
    count = 0
    while temp is not None:
        count = count+1
        temp = temp.next
    return count

def copy(head):
    copyHead = []
    temp = head.head
    while temp != None:
        x = temp.data
        copyHead.append(x)
        temp = temp.next
    return copyHead

def copyList(head):
    copyList = LinkedList()
    temp = head.head
    while temp != None:
        copyList.append(temp.data)
        temp = temp.next
    return copyList

def insertLL(head, llist, index):
    temp = head.head
    temp2 = llist.head
    count = 0
    while temp != None:
        if count == index-1:
            if temp.next == None:
                temp.next = temp2
            else:
                nextNode = temp.next 
                temp.next = temp2
                while temp2.next != None:
                    temp2 = temp2.next
                temp2.next = nextNode
        count += 1
        temp = temp.next
        


def scarmble(head, b, r, size):

    count = 0
    count2 = 0
    count3 = 0
    count4 = 0

    print("BottomUp %.3f"%(b)+ " % : ", end='')
    x = int((size * float(b))/100)
    for i in range(x):
        head.append(head.popFirstNode().data)
    printLL(head)
    
    print("Riffle %.3f"%(r)+ " % : ", end='')
    y = int((size * float(r))/100)
    for i in range(size):
        if i < y:
            pass
        else:
            if count2  == y:
                break
            temp = head.deleteByPosition(i)
            head.insertAfterByPo(count, temp)
            count = count+2
            count2 = count2+1
    printLL(head)
    
    print("Deriffle %.3f"%(r)+ " % : ", end='')
    
    index = y
    llist = LinkedList()
    for i in range(size):
        if i == 0:
            pass
        else:
            if count3  == count2:
                break
            temp = head.deleteByPosition(i)
            llist.append(str(temp))
            count3 = count3+1
    
    insertLL(head, llist, index)
    printLL(head)

    print("Debottomup %.3f"%(b)+ " % : ", end='')
    for i in range(size):
        if i < size-x:
            pass
        else:
            temp = head.deleteByPosition(i)
            if i == size-x:
                head.push(str(temp))
            else:
                head.insertAfterByPo(count4, temp)
                count4 = count4+1

    printLL(head)
           

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : ", end='')
    printLL(h)
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)