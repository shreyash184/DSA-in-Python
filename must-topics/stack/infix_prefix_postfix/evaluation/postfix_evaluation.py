from queue import deque 


def is_digit(c):
    if c >= '0' and c <= '9':
        return 1
    return 0

def operations(c, a, b):
    if c == '+':
        return a + b 
    elif c == '-':
        return a - b 
    elif c == '*':
        return a * b 
    elif c == '/':
        return a / b 

def postfix_evaluation(s):
    stack = deque()

    for c in s:
        if is_digit(c):
            stack.append(c)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            curr = operations(c, int(op1), int(op2))
            stack.append(curr)
    return stack.pop()



s = "2536+**5/2-"
print(postfix_evaluation(s))