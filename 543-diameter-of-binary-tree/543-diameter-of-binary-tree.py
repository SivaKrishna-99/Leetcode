# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self,root:Optional[TreeNode]) -> int:
        diameter = [0]
        
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            diameter[0] = max(diameter[0],2+left+right)
            
            return 1+max(left,right)
        dfs(root)
        return diameter[0]
        
        