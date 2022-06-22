class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = -1
        for i in range(len(arr)-1,-1,-1):            
            newMax = max(maxVal,arr[i])
            arr[i] = maxVal
            maxVal = newMax
        return arr
            
            
        