# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        ans = []
        self.helperDfs(root, "", ans)
        return ans
    
    def helperDfs(self, root, String, ans):
        String += str(root.val)
        if not root.left and not root.right:
            ans.append(String)
        if root.left:
            self.helperDfs(root.left,String+'->',ans)
        if root.right:
            self.helperDfs(root.right,String+'->', ans)
        
        