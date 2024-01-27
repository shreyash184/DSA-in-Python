from queue import deque

def isOperand(c):
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
        return 1
    return 0

def postfix_to_infix(s):
    stack = deque()

    for c in s:
        if isOperand(c):
            stack.append(c)
        else: 
            op2 = stack.pop()
            op1 = stack.pop()
            curr = '(' + op1 + c + op2 + ')'
            stack.append(curr)
    return stack.pop()

# s = "AB*C+"
s = "abc++"
print(postfix_to_infix(s))