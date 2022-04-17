class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0]*3
        for i in range(len(nums)):
            if nums[i] == 0:
                freq[0] += 1
            elif(nums[i] == 1):
                freq[1] += 1
            else:
                freq[2] += 1
        
        i = 0
        while freq[0] >0:
            nums[i] = 0
            i += 1
            freq[0] -= 1
        while freq[1]>0:
            nums[i] = 1
            i += 1
            freq[1] -= 1
        while freq[2] > 0:
            nums[i] = 2
            i += 1
            freq[2] -= 1
            
     
        
        
            
                
                
                
                
                
        