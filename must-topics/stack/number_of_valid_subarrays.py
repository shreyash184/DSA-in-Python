from queue import deque

def validSubarrays(list):
    n = len(list)
    stack = deque()
    total_contribution = 0

    for i in range(n):
        while len(stack) > 0 and list[stack[-1]] > list[i]:
            curr = stack.pop()
            nse = i 
            contribution = nse - curr 
            total_contribution += contribution
        stack.append(i) 

    while len(stack) > 0:
        curr = stack.pop()
        nse = n
        contribution = nse - curr 
        total_contribution += contribution

    return total_contribution

# list = [1,4,2,5,3]
# list = [3,2,1]
list = [2,2,2]
print(validSubarrays(list))