stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

print(f"Top element - {stack[-1]}")
print(len(stack))


print('\nElements popped from stack: ')
print(stack.pop())
print(stack.pop())
print(stack.pop())
