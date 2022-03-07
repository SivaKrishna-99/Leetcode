# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        out = []
        q = collections.deque()
        q.append(root)
        
        while q:
            
            list_size = len(q)
            temp = []
            for i in range(list_size):
                node = q.popleft()
                if node:
                    temp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if temp:        
                out.append(temp)
        return out
                
            
            
            
            
            