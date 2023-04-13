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

    def huffman(self, inp):
        
        lis = []

        dic = {}

        freq = []

        for i in inp:
            if i in lis:
                pass
            else:
                lis.append(i)
                count = inp.count(i)
                freq.append(count)
                dic[str(i)] = count


inp = input("Enter input : ")