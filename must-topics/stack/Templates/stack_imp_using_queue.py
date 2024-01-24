queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print("Initial queue")
print(queue)

print(f"size of queue is {len(queue)}")
print(f"front element of queue is {queue[0]}")
print(f"rear element of queue is {queue[-1]}")

print("\nElement dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))