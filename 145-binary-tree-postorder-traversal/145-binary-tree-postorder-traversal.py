# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.postorderHelper(root,out)
        return out
    def postorderHelper(self,root,out):
        if root:
            self.postorderHelper(root.left,out)
            self.postorderHelper(root.right,out)
            out.append(root.val)