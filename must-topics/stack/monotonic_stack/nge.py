from collections import deque

# input - list - [4, 5, 25, 3]
# output -  [5, 25, -1, -1]

def nge(list):
    n = len(list)
    ans = [-1] * n

    stack = deque()

    for i in range(0, n):
        while len(stack) > 0 and list[stack[-1]] < list[i]:
            ans[stack[-1]] = list[i]
            stack.pop()
        stack.append(i)

    while len(stack) > 0:
        ans[stack.pop()] = -1
    return ans

# list = [4, 5, 2, 25]
list = [11, 4, 3, 2, 10, 12]
# list = [10, 7, 4, 2, 9, 10, 11, 3, 2] - Dry run test case
print(nge(list))
