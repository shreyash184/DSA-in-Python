from queue import deque

def prec(c):
    if c == '^':
        return 3
    elif c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return 0

def isOperand(c):
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and  c <= '9'):
        return 1 
    return 0

def infix_to_postfix(s):
    stack = deque()

    postfix = ""
    for c in s:
        if isOperand(c):
            postfix += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while len(stack) > 0 and prec(stack[-1]) >= prec(c):
                postfix += stack.pop()
            stack.append(c)

    while len(stack) > 0:
        postfix += stack.pop()
    
    return postfix


# s = "A+B-C"
s = "(A+B)*C-D"
print(infix_to_postfix(s))