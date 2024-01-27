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

def infix_to_prefix(str):
    str = str[::-1]
    stack = deque()
    s = ""

    for i in range(len(str)):
        if str[i] == '(':
            s += ')'
        elif str[i] == ')':
            s += '('
        else:
            s += str[i]

    prefix = ""

    for c in s:
        if isOperand(c):
            prefix += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                prefix += stack.pop()
            stack.pop()
        else:
            while len(stack) > 0 and prec(stack[-1]) >= prec(c):
                prefix += stack.pop()
            stack.append(c)
    
    while len(stack) > 0:
        prefix += stack.pop()

    return prefix[::-1]



s = "A*B+C/D"
# s = "(A-B/C)*(A/K-L)"
print(infix_to_prefix(s))