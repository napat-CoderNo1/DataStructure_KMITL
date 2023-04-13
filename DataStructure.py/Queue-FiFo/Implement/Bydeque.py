from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')

# print(len(q))

# for i in range(0, len(q),1):
#     print(i)

print("Initial queue")
print(q)

print("\nElements dequeued from the queue")
# pop() ใน deque จะเป็นการ pop เอาตัวท้ายสุดออก เเละ ไม่มี pop(0)
print(q.popleft())
print(q.popleft())
print(q.popleft())
 
print("\nQueue after removing elements")
print(q)