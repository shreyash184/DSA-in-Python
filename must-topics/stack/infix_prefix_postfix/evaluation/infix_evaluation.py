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

def infix_evaluation(s):
    operator_stack = deque()
    operand_stack = deque()

    for c in s:
        if is_digit(c):
            operand_stack.append(int(c))
        elif c == '(':
            operator_stack.append(c)
        elif c == ')':
            while operator_stack[-1] != '(':
                operator = operator_stack.pop()
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                curr = operations(operator, int(op1), int(op2))
                operand_stack.append(int(curr))
            operator_stack.pop()
        else:
            while len(operator_stack) > 0 and prec(operator_stack[-1]) >= prec(c):
                operator = operator_stack.pop()
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                curr = operations(operator, int(op1), int(op2))
                operand_stack.append(int(curr))
            operator_stack.append(c)
    
    while len(operator_stack) > 0:
        operator = operator_stack.pop()
        op2 = operand_stack.pop()
        op1 = operand_stack.pop()
        curr = operations(operator, int(op1), int(op2))
        operand_stack.append(int(curr))

    return operand_stack.pop()



s = "2*5+(2*3)"
# s = "2*(5*(3+6))/5-2+2+5+(5*5)"
print(infix_evaluation(s))