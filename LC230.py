# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        n = 0

        while True:
            if root:
                stk.append(root)
                root = root.left

            else:
                root = stk.pop()
                n+=1
                print(root.val, n, k)
                if n == k:
                    return root.val

                root = root.right
