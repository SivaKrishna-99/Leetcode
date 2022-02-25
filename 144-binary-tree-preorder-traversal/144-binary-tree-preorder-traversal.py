# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.preorderHelper(root,out)
        return out
    def preorderHelper(self, root,out):
        if root:
            out.append(root.val)
            self.preorderHelper(root.left,out)
            self.preorderHelper(root.right,out)
        