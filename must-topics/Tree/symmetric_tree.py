class Solution:

    def check(self, l, r):
        if not l and not r:
            return True
        
        if not l or not r:
            return False

        return l.val == r.val and self.check(l.left, r.right) and self.check(l.right, r.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check(root, root)