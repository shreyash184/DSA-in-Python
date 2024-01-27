from queue import deque

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

def pge(list):
    list.reverse()
    ans = nge(list)
    ans.reverse()
    return ans

list = [10, 4, 2, 20, 40, 12, 30]
print(pge(list))