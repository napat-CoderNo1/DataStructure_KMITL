# Dynamic data มาก resource มาก
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        
        if left == None:
            self.left = None
        else:
            self.left = left

        if right == None:
            self.right = None
        else:
            self.right = right