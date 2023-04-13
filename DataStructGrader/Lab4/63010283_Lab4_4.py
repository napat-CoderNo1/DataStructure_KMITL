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


myQueue = Queue()
yourQueue = Queue()

Activity = {"0":"Eat", "1":"Game", "2":"Learn", "3":"Movie"}
Location = {"0":"Res.", "1":"ClassR.", "2":"SuperM.", "3":"Home"}

point = 0

inp = input("Enter Input : ").split(",")

for i in range(0, len(inp), 1):
    myQueue.enQueue(inp[i][0:3])

for i in range(0, len(inp), 1):
    yourQueue.enQueue(inp[i][4:])

print("My   Queue = ", end='')

for i in range(0, myQueue.size(), 1):
        if i == myQueue.size()-1:
            print(myQueue.items[i])
        else:
            print(myQueue.items[i]+", ", end='')

print("Your Queue = ", end='')

for i in range(0, yourQueue.size(), 1):
        if i == yourQueue.size()-1:
            print(yourQueue.items[i])
        else:
            print(yourQueue.items[i]+", ", end='')

print("My   Activity:Location = ", end='')

for i in range(0, myQueue.size(), 1):
    print(Activity[myQueue.items[i][0]], end=':')
    print(Location[myQueue.items[i][2]], end='')
    if i == myQueue.size()-1:
        print("")
    else:
        print(", ", end='')

print("Your Activity:Location = ", end='')

for i in range(0, yourQueue.size(), 1):
    print(Activity[yourQueue.items[i][0]], end=':')
    print(Location[yourQueue.items[i][2]], end='')
    if i == yourQueue.size()-1:
        print("")
    else:
        print(", ", end='')

# point
for i in range(0, myQueue.size(), 1):
    # same Activity
    if myQueue.items[i][0] == yourQueue.items[i][0]:
        # same Location
        if myQueue.items[i][2] == yourQueue.items[i][2]:
            point = point+4
        # diff location
        else:
            point = point+1
    elif myQueue.items[i][2] == yourQueue.items[i][2]:
        point = point+2
    else:
        point = point-5

# check point
if point >= 7:
    print("Yes! You're my love! : Score is "+str(point)+".")
elif point >= 0:
    print("Umm.. It's complicated relationship! : Score is "+str(point)+".")
else:
    print("No! We're just friends. : Score is "+str(point)+".")