queue = []

queue.append('a')
queue.append('b')
queue.append('c')

# print(queue[0])

print("Initial queue")
print(queue)

print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)