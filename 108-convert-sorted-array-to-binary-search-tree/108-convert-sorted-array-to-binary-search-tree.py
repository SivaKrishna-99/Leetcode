# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        l,r = 0,len(nums)-1
        return self.helper(nums,l,r)
    
    def helper(self,nums, l,r):
        if l > r:
            return None
        mid = l+ (r-l)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums,l,mid-1)
        root.right = self.helper(nums, mid+1,r)
        return root
        

    
        
        
        