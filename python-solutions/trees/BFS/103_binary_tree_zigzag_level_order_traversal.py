from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        result = []
        level = 0
        queue.append((root, level))

        while queue:
            temp = []
            l = len(queue)
            for i in range(l):
                elem, level = queue.popleft()
                temp.append(elem.val)
                if elem.left:
                    queue.append((elem.left, level + 1))
                if elem.right:
                    queue.append((elem.right, level + 1))

            if level % 2 == 0:
                result.append(temp)
            else:
                temp.reverse()
                result.append(temp)

        return result
