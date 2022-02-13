class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        left = 0
        right = 1
        while right < len(prices):
            if (prices[right] > prices[left]) :
                temp = prices[right]-prices[left]
                # diff = max(diff,temp)
                if (temp > diff):
                    diff = temp    
            else : 
                left = right
            right += 1       
        return diff
        
        