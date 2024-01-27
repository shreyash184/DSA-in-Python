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

list = [[1,0,1,0,0],
        [1,0,1,1,1],
        [1,1,1,1,1],
        [1,0,0,1,0]
        ]

for i in range(1, 4):
    for j in range(5):
        if list[i][j] == 1:
            list[i][j] += list[i-1][j]

max_rec = 0

for i in range(4):
    max_rec = max(max_rec, largestRectangleArea(list[i]))

print(max_rec)
