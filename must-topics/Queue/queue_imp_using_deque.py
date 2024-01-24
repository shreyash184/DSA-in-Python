from collections import deque 

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print("Initial queue")
print(queue)

print(f"size of queue {len(queue)}")
print(f"front element of queue {queue[0]}")
print(f"rear element of queue {queue[-1]}")

print("dequeing the element of queue")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())