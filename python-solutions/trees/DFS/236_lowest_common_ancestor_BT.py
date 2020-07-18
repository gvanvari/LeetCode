class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # in this is case either p or q are none then we are returning 1 of them
        # but if both p and q should not be none i.e if either 1 of them is none return none, create a helper function which search for p and q first
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right

    # last return statment takes care of 3 if conditions -
    # 1. left none or right none
    # 2. both none
    # 3. p and q are not found anywhere
