# x = input("Enter code,hint : ").split(",")

# hint = x[0][0]
# first = x[1]

# distance = ord(first) - ord(hint)

# for i in x[0]:
#     print(chr(ord(i)+distance), end='')

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enQueue(self, new_data):
        self.items.append(new_data)

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Popping from an empty queue")
        return self.items.popleft()

    def isEmpty(self):
        return len(self.items) == 0

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


q = Queue()

x = input("Enter code,hint : ").split(",")

hint = x[0][0]
first = x[1]

distance = ord(first) - ord(hint)

for i in range(0, len(x[0]), 1):
    q.enQueue(chr(ord(x[0][i])+distance))
    print("[", end='')
    for i in range(0, q.size(), 1):
        if i == q.size()-1:
            print("'"+q.items[i]+"'", end='')
            print("]")
        else:
            print("'"+q.items[i]+"', ", end='')