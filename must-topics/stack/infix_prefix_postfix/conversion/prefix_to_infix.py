from queue import deque 

def isOperand(c):
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and  c <= '9'):
        return 1 
    return 0

def isOperator(c):
    if (c == '+' or c == '-' or c == '*' or c == '/'):
        return 1
    return 0

def prefix_to_infix(s):
    s = s[::-1]

    stack = deque()

    for c in s:
        if isOperand(c):
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            curr = '(' + op1 + c + op2 + ')'
            stack.append(curr)

    return stack.pop()

s = "*+AB-CD"
s = "*-A/BC-/AKL"
print(prefix_to_infix(s))