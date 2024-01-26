from collections import deque

def ngeII(list):
    n = len(list)
    ans = [-1] * n

    stack = deque()

    for i in range(2*n):
        j = i % n
        while stack and list[stack[-1]] < list[j]:
            ans[stack.pop()] = list[j]
        stack.append(j)

    # while len(stack) > 0:
    #     ans[stack.pop()] = -1
    return ans

list = [5, 4, 3, 2, 1]
print(ngeII(list))