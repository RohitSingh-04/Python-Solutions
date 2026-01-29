# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        stack = [[root, 1]]

        while stack:

            node, current_level = stack.pop()

            if node.left:
                stack.append([node.left, current_level+1])

            if node.right:
                stack.append([node.right, current_level+1])
            
            level = max(level, current_level)

        return level