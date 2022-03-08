# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        # res = []
        # node = root
        # def preorder(root):
        #     if root:
        #         res.append(root)
        #         preorder(root.left)
        #         preorder(root.left)
        # preorder(root)
        # i = 1
        # while node and i < len(res):
        #     node.right = res[i]
        #     node.left = None
        #     node = node.right
        #     i += 1
        stack = deque()
        stack.append(root)
        while stack :
            curr_node = stack.pop()
            if curr_node.right != None:
                stack.append(curr_node.right)
            
            if curr_node.left != None:
                stack.append(curr_node.left)
            if stack:
                curr_node.right = stack[-1]
            curr_node.left = None
        
        
       
            
            
        