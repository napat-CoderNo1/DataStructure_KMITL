class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

    def print(self):
        print(self.key)

class Hash:
    def __init__(self, table_size, max_collision, threshold):
        self.table_size = table_size
        self.max_collision = max_collision
        self.threshold = threshold
        self.table = [None]*self.table_size
        self.list = []
    
    def hash_value(self, key): # key = string
        ascii = 0
        ascii = ascii + int(key)
        index = ascii % self.table_size
        return index

    def isTH(self):
        count = 0
        for i in range(len(self.table)):
            if self.table[i] != None:
                count+=1
        return count >= int((self.threshold/100)*self.table_size)

    def isFull(self):
        count = 0
        for i in range(len(self.table)):
            if self.table[i] != None:
                count+=1
        return count == self.table_size

    def isPrime(self, num):
        flag = True
        
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = False
                    break

        return flag
    
    def rehash(self):
        # l = []
        # for i in range(self.table_size):
        #     if self.table[i] != None:
        #         l.append(self.table[i])

        table_size = self.table_size * 2
        while self.isPrime(table_size) is False:
            table_size +=1
        self.table = [None]*table_size
        # if self.table_size == 7:
        #     print(self.table)
        self.table_size = table_size
    
        # print(self.list)
        for i in self.list:
            self.insert(i, False)

    
    def insert(self, data, first = True): # data = object
        
        if self.isFull():
            print("This table is full !!!!!!")
            return 'x'
        # print(int((self.threshold/100)*self.table_size))

        count = 0
        while count < self.max_collision:
            if first == True:
                print("Add :", data.value)
                first = False
            
            if self.isTH():
                print("****** Data over threshold - Rehash !!! ******")
                # self.rehash()
                self.rehash()

            index = (self.hash_value(data.key) + (count*count)) % self.table_size
            
            if self.table[index] is None:
                self.table[index] = data # object
                return
            
            count += 1
            print("collision number", count, "at", index)
        
        print("****** Max collision - Rehash !!! ******")
        # return 'H'
        self.rehash()
        self.insert(data, False)
        # self.insert(data, first)

    def __str__(self):
        text = ''
        for i in range(self.table_size):
            if self.table[i] is None:
                text += "#" + str(i+1) + "\t" + str(self.table[i]) + "\n"
            else:
                text += "#" + str(i+1) + "\t" + str(self.table[i].value) + "\n"
        text += '----------------------------------------'
        return text


print(" ***** Rehashing *****")

left, right = input("Enter Input : ").split("/")

table_size, max_collision, threshold = list(map(int, left.split()))

# print(table_size)        5
# print(max_collision)     1
# print(threshold)        67

temp = right.split()
# print(temp) => ['1','6']

data_lis = []

for i in temp:
    # print(type(i))
    key = i
    value = i
    data_lis.append(Data(key, value))

table = Hash(table_size, max_collision, threshold)

print("Initial Table :")
print(table)

for i in data_lis:
    x = table.insert(i, True)
    # if x == 'H':
    #     table.rehash()
    #     for j in data_lis:
    #         x = table.insert(j, False)
    print(table)
    table.list.append(i)