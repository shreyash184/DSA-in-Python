from queue import deque


def sumSubarrayMins(list):
    stack = deque()
    stack.append(-1)
    n = len(list)
    total_contribution = 0

    for i in range(n):
        while stack[-1] != -1 and list[stack[-1]] > list[i]:
            curr = stack.pop()
            pse = stack[-1]
            nse = i 
            contribution = list[curr] * (curr-pse) * (nse-curr)
            total_contribution = (total_contribution + contribution) % (10 ** 9 + 7)
        stack.append(i)

    while stack[-1] != -1:
        curr = stack.pop()
        pse = stack[-1]
        nse = n 
        contribution = list[curr] * (curr-pse) * (nse-curr)
        total_contribution = (total_contribution + contribution) % (10 ** 9 + 7)
    return total_contribution % (10 ** 9 + 7)

list = [3, 1, 2, 4]
print(sumSubarrayMins(list))