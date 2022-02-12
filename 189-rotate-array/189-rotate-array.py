class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """       
#         n = len(nums)     #TLE
#         while k > 0:
#             prev = nums[-1]
#             for i in range(len(nums)):
#                 temp = nums[i]
#                 nums[i] = prev
#                 prev = temp
#                 i += 1
#             k -= 1
            
        k = k % len(nums)
        count = 0
        begin = 0
        while count < len(nums):# used just for one pass
            curr = begin 
            prev = nums[begin] 
            
            while True:
                next = (curr + k) % len(nums) #
                temp = nums[next]
                nums[next] = prev
                prev = temp 
                curr = next 
                count += 1

                if begin == curr:
                    break 
            
            begin += 1
    
            