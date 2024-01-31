class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque()

        q.append(root)
        q.append(None)

        ans = list()
        prev = root
        curr = root

        while len(q) > 0:
            curr = q.popleft()
            while curr is not None:

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

                prev = curr
                curr = q.popleft()
            ans.append(prev.val)

            if len(q) > 0:
                q.append(None)
            
        return ans 