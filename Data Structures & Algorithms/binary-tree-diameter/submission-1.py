# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(root):
            nonlocal result
            if not root:
                return 0
            left_count = dfs(root.left)
            right_count = dfs(root.right)
            d = left_count + right_count
            result = max(result , d)
            return 1+ max(left_count, right_count) 
        dfs(root)
        return result