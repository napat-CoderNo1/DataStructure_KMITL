class Queue1:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, new_Data):
        self.items.append(new_Data)

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Popping from an empty queue")
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def isFull(self):
        pass

    def size(self):
        return len(self.items)

    def front(self):
        if self.isEmpty():
            raise Exception("empty queue")
        return self.items[0]

    def tail(self):
        if self.isEmpty():
            raise Exception("empty queue")
        return self.items[-1]


q = Queue1()

q.enQueue('A')
q.enQueue('B')
print(q.items[0])