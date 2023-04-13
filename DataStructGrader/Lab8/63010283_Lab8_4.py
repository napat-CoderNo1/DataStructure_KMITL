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

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

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

    def Favonius(self, groupNumber, lis = []):

        groupNumber = int(groupNumber)

        self.insert(lis[int(groupNumber)])

        if (2*groupNumber)+1 <= len(lis)-1:
            self.insert(lis[(2*groupNumber)+1])
        if (2*groupNumber)+2 <= len(lis)-1:
            self.insert(lis[(2*groupNumber)+2])

    def Power(self, root):
        if root == None:
            return 0
        return root.data + self.Power(root.left) + self.Power(root.right)
        

inp = input("Enter Input : ").split("/")

inp[0] = inp[0].split()
inp[1] = inp[1].split(",")

temp = [inp[1][i].split() for i in range(len(inp[1]))]
# print(temp)

for i in range(len(inp[0])):
    inp[0][i] = int(inp[0][i])

# print(inp[0])

print(sum(inp[0]))

T1 = BST()
T2 = BST()

# T1.Favonius(1,inp[0])
# T1.printTree(T1.root)
# print(T1.Power(T1.root))
# T1 = BST()
# T1.printTree(T1.root)
for i in range(len(temp)):
    T1.Favonius(temp[i][0], inp[0])
    T2.Favonius(temp[i][1], inp[0])
    if T1.Power(T1.root) > T2.Power(T2.root):
        print(str(temp[i][0])+'>'+str(temp[i][1]))
    elif T1.Power(T1.root) < T2.Power(T2.root):
        print(str(temp[i][0])+'<'+str(temp[i][1]))
    elif T1.Power(T1.root) == T2.Power(T2.root):
        print(str(temp[i][0])+'='+str(temp[i][1]))
    T1 = BST()
    T2 = BST()