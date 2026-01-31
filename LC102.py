# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = deque([root])

        while q:
            current_level = []
            for _ in range(len(q)):
                root = q.popleft()
                if root:
                    current_level.append(root.val)
                    q.append(root.left)
                    q.append(root.right)
            if len(current_level):
                result.append(current_level)
        return result