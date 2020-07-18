from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# two concepts - queue and BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        level = []  # queue

        result = []

        level.append(root)

        while level:
            temp = []  # leetcode wants list of list i.e why used temp
            l = len(level)
            for i in range(l):
                elem = level.pop(0)
                temp.append(
                    elem.val)  # if temp is not used then result will be [3,9,20,15,7] but we need [3,[9,20],[15,7]]

                if elem.left:
                    level.append(elem.left)

                if elem.right:
                    level.append(elem.right)

            result.append(temp)

        return result
