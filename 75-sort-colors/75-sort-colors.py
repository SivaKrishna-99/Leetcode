class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #One-Pass Solution
        left,right = 0,len(nums)-1
        p = 0
        
        while p <= right:
            if nums[p] == 0:
                nums[p],nums[left] = nums[left],nums[p]
                left += 1
            elif(nums[p] == 2):
                nums[p],nums[right] = nums[right],nums[p]
                right -= 1
                p -= 1
            p += 1
            
                
                
                
        
        # #Two Pass Solution
        # freq0,freq1,freq2 = 0,0,0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         freq0 += 1
        #     elif(nums[i] == 1):
        #         freq1 += 1
        #     else:
        #         freq2 += 1
        # i = 0
        # while freq0 > 0:
        #     nums[i] = 0
        #     i += 1
        #     freq0 -= 1
        # while freq1>0:
        #     nums[i] = 1
        #     i += 1
        #     freq1 -= 1
        # while freq2 > 0:
        #     nums[i] = 2
        #     i += 1
        #     freq2 -= 1
        #Bucket Sort
#         freq = [0]*3
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 freq[0] += 1
#             elif(nums[i] == 1):
#                 freq[1] += 1
#             else:
#                 freq[2] += 1
        
#         i = 0
#         while freq[0] >0:
#             nums[i] = 0
#             i += 1
#             freq[0] -= 1
#         while freq[1]>0:
#             nums[i] = 1
#             i += 1
#             freq[1] -= 1
#         while freq[2] > 0:
#             nums[i] = 2
#             i += 1
#             freq[2] -= 1
            
     
        
        
            
                
                
                
                
                
        