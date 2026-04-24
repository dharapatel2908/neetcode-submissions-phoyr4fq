# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        result = 0
        def dfs(node):
            nonlocal count, result
            if not node:
                return
            dfs(node.left)
            count-=1
            if count ==0:
                result = node.val
            # if not dfs(node.left):
            #     dfs(node.right)
            #     if count ==0:
            #         result = node.val
            #     count -=1
            dfs(node.right)
            # count-=1
            # if count ==0:
            #     result = node.val
            
            # if not dfs(node.right):
            #     dfs(node.left)
            #     if count ==0:
            #         result = node.val
            #     count -=1   
            
            return result
        return dfs(root)