from queue import deque

def nse(list):
    n = len(list)
    ans = [-1] * n

    st = deque()

    for i in range(0, n):
        while len(st) > 0 and list[st[-1]] > list[i]:
            ans[st[-1]] = list[i]
            st.pop()
        st.append(i)
    
    while len(st) > 0:
        ans[st.pop()] = -1

    return ans 

list = [4, 6, 10, 5, 2]
print(nse(list))