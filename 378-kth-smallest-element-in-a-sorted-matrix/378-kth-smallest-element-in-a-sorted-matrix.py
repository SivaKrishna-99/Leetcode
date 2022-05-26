class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        array = []
        for val in matrix:
            array.extend(val)
        array.sort()
        return array[k-1]
        
        