# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = deque()
        curr = head
        ans=[0] * 10001
        i = 0
        while curr:
            while len(stack) > 0 and stack[-1].val < curr.val:
                ans[stack[-1].idx] = curr.val
                stack.pop()
            stack.append(Node(curr.val, i))
            curr = curr.next
            i += 1
        while len(stack) > 0:
            ans[stack.pop().idx] = 0

        return ans[0:i]