from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print(f"Current element in stack {stack}")
print(f"Size of stack - {len(stack)}")
print(f"Top element of stack - {stack[-1]}")

print("popping all the elements")
print(stack.pop())
print(stack.pop())
print(stack.pop())