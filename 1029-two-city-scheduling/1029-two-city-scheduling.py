class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        len_costs = len(costs)
        sumA = 0
        for i in range(len_costs):
            sumA += costs[i][0]
        diff = []
        for i in range(len_costs):
            diff.append(costs[i][1]-costs[i][0])
        
        diff.sort()
        min_cost = sumA
        for i in range(len_costs//2):
            min_cost += diff[i]
        return min_cost
        