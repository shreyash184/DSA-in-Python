from queue import deque

def isOperand(c):
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and  c <= '9'):
        return 1 
    return 0

def prefix_to_postfix(s):
    s = s[::-1]
    stack = deque()

    for c in s:
        if isOperand(c):
            stack.append(c)
        else:
            first = stack.pop()
            second = stack.pop()
            curr = first + second + c 
            stack.append(curr)
    return stack.pop() 

# s = "-*+ABCD"
s = "-+ABC"
print(prefix_to_postfix(s))