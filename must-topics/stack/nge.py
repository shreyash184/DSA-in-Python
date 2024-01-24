from collections import deque

# input - list - [4, 5, 25, 3]
# output -  [5, 25, -1, -1]

def nge(list):
    ans = [-1] * len(list)

    stack = deque()

    stack.append(0)
    for i in range(1, len(list)):
        while len(stack) > 0 and list[i] > list[stack[-1]]:
            ans[stack[-1]] = list[i]
            stack.pop()
        stack.append(i)

    while len(stack) > 0:
        topIndx = stack[-1]
        ans[topIndx] = -1
        stack.pop()

    print(ans)

list = [4, 5, 25, 3]
nge(list)
