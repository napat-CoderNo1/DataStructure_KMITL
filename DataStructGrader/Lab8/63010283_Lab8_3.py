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
            if temp.data <= data:
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

    def rank(self, node, data):
        if node.right is None and node.left is None:
            if data >= node.data:
                return 1
            else:
                return 0
        elif node.right is None:
            if data >= node.data:
                return self.rank(node.left, data) + 1
            else:
                return self.rank(node.left, data) 
        elif node.left is None:
            if data >= node.data:
                return self.rank(node.right, data) + 1
            else:
                return self.rank(node.right, data)
        else:
            if data >= node.data:
                return self.rank(node.right, data) + self.rank(node.left, data)+1
            else:
                return self.rank(node.left, data)


T = BST()
inp = [i.split() for i in input('Enter Input : ').split("/")]

for i in range(len(inp[0])):
    inp[0][i] = int(inp[0][i])

for i in inp[0]:
    root = T.insert(i)
T.printTree(root)

print("--------------------------------------------------")

print("Rank of "+ inp[1][0] + " : ", end='')
print(T.rank(root, int(inp[1][0])))