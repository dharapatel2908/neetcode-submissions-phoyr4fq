# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
# Pre order = root, left, right
#inOrder = left, root, right
#                   |
#                   mid
        if not preorder or not inorder:
            return None
        root_value = preorder[0]
        root = TreeNode(root_value)
        middle_root =inorder.index(root_value)
        root.left= self.buildTree(preorder[1:middle_root+1],inorder[:middle_root])
        root.right = self.buildTree(preorder[middle_root+1:], inorder[middle_root+1:])
        return root

