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

def pse(list):
    list.reverse()
    ans = nse(list)
    ans.reverse()
    return ans

list = [10, 4, 2, 20, 40, 12, 30]
print(pse(list))