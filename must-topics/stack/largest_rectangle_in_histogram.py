from queue import deque

def largestRectangleArea(height):
    stack = deque()
    stack.append(-1)
    max_area = 0

    for i in range(0, len(height)):
        while stack[-1] != -1 and height[stack[-1]] >= height[i]:
            current_height = height[stack.pop()]
            pse = stack[-1]
            nse = i 
            max_area = max(max_area, current_height * (nse - pse - 1))

        stack.append(i)
    
    while stack[-1] != -1:
        current_height = height[stack.pop()]
        pse = stack[-1]
        nse = len(height) 
        max_area = max(max_area, current_height * (nse - pse - 1))
    return max_area

height = [2,1,5,6,2,3]
print(largestRectangleArea(height))

