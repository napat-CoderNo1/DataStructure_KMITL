class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, table_size, max_collision):
        self.table_size = table_size
        self.max_collision = max_collision
        self.table = [None]*table_size
    
    def hash_value(self, key): # key = string
        ascii = 0
        for i in key:
            ascii = ascii + ord(i)
        index = ascii % self.table_size
        return index

    def isFull(self):
        count = 0
        for i in range(len(self.table)):
            if self.table[i] != None:
                count+=1
        return count == self.table_size

    def insert(self, data): # data = object
        if self.isFull():
            print("This table is full !!!!!!")
            return 'x'
        
        count = 0
        while count < self.max_collision:
            index = (self.hash_value(data.key) + (count*count)) % self.table_size
            
            if self.table[index] is None:
                self.table[index] = data # object
                return
            
            count += 1
            print("collision number", count, "at", index)
        
        print("Max of collisionChain")

    def __str__(self):
        text = ''
        for i in range(self.table_size):
            text += "#" + str(i+1) + "\t" + str(self.table[i]) + "\n"
        text += '---------------------------'
        return text



print(" ***** Fun with hashing *****")

left, right = input("Enter Input : ").split('/')
table_size, max_collision = list(map(int, left.split()))

# print(table_size)
# print(max_collision)

temp = right.split(",")
data_lis = []

for i in temp:
    # print(i)
    key, value = i.split()
    data_lis.append(Data(key, value))

table = Hash(table_size, max_collision)

for i in data_lis:
    x = table.insert(i)
    if x == 'x':
        break
    print(table)
