class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, None, None)

    def validate(self, root, low, high):
        if not root:
            return True

        if (low is not None and root.val <= low) or (high is not None and root.val >= high):
            return False

        return self.validate(root.left, low, root.val) and self.validate(root.right, root.val, high)