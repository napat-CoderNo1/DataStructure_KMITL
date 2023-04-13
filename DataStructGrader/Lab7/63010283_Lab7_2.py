class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        if self.root is None:
            self.root = Node(data)
            return self.root
        temp = self.root
        while True:
            if temp.data < data:
                if temp.right is None:
                    temp.right = Node(data)
                    break
                else:
                    temp = temp.right
            else:
                if temp.left is None:
                    temp.left = Node(data)
                    break
                else:
                    temp = temp.left
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkLessThan(self, node, number, q=[]):
        if node != None:
            self.checkLessThan(node.left, number, q)
            if node.data < number:
                q.append(node.data)
            self.checkLessThan(node.right, number, q)
        
        return q


T = BST()
inp = [ i.split() for i in input('Enter Input : ').split("|")]

for i in range(0, len(inp[0]), 1):
    inp[0][i] = int(inp[0][i])

for i in inp[0]:
    root = T.insert(i)
T.printTree(root)

print("--------------------------------------------------")

print("Below", end=' ')
print(inp[1][0], end=' : ')

temp = T.checkLessThan(root, int(inp[1][0]), q = [])

if len(temp) == 0:
    print("Not have", end='')
else:
    for i in temp:
        print(i, end=' ')