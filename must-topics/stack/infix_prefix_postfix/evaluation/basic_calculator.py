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
    s = s.replace(" ", "")
    operator_stack = deque()
    operand_stack = deque()
    if s[0] == '-':
        operand_stack.append(0)
    i = 0

    while i < len(s):
        if is_digit(s[i]):
            num = s[i] 
            while (i < len(s) - 1) and is_digit(s[i+1]):
                num += s[i+1]
                i += 1
            operand_stack.append(int(num))
        elif s[i] == '(':
            operator_stack.append(s[i])
            if i+1 < len(s) and s[i+1] == '-':
                operand_stack.append(0)
        elif s[i] == ')':
            while operator_stack[-1] != '(':
                operator = operator_stack.pop()
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                curr = operations(operator, int(op1), int(op2))
                operand_stack.append(int(curr))
            operator_stack.pop()
        else:
            while len(operator_stack) > 0 and prec(operator_stack[-1]) >= prec(s[i]):
                operator = operator_stack.pop()
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                curr = operations(operator, int(op1), int(op2))
                operand_stack.append(int(curr))
            operator_stack.append(s[i])
        i+=1
    
    while len(operator_stack) > 0:
        operator = operator_stack.pop()
        op2 = operand_stack.pop()
        op1 = operand_stack.pop()
        curr = operations(operator, int(op1), int(op2))
        operand_stack.append(int(curr))

    return operand_stack.pop()


# s = "11+(4+5+2)-3)+(6+8)"
# s = "11+(4+5+2)"
s = "2*50+(2*3)-4"
# s = "2*(5*(3+6))/5-2+2+5+(5*5)"
print(infix_evaluation(s))