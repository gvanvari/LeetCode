class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        #         if not t1 and not t2:
        #             return None

        #         if not t2:
        #             return t1

        #         if not t1:
        #             return t2

        if not t1 or not t2:
            return t1 or t2

        t1.val = t1.val + t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1
