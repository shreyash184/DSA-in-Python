from queue import deque

def remove_duplicate_letters(s):
    stack = deque()
    seen = set()
    last_occ = dict()

    for i in range(len(s)):
        last_occ[s[i]] = i 
    
    for i in range(len(s)):
        c = s[i]
    
        if c not in seen:
            while len(stack) > 0 and c < stack[-1] and last_occ[stack[-1]] > i:
                seen.remove(stack.pop())
            seen.add(c)
            stack.append(c)
    
    ans = ""
    while len(stack) > 0:
        ans += stack.pop()
    return ans[::-1]


s = "bcabc"
print(remove_duplicate_letters(s))