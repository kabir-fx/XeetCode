class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        DP

        Intuition - For each step we will calculate the cost associated to that corresponding index. At each index we will make the choice to decide the path 1 or 2 which has the minimum cost.
        """
        
        for i in reversed(range(len(cost) - 2)):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
                    
            
# O(n)
# O(1)
