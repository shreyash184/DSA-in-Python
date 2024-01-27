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
    
def prefix_evaluation(s):
    s = s[::-1]
    stack = deque()

    for c in s:
        if is_digit(c):
            stack.append(int(c))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            cur = operations(c, int(op1), int(op2))
            stack.append(cur)
    return stack.pop()

# s = "-+8/632"
s = "-+7*45+20"
print(prefix_evaluation(s))