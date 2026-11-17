class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

    #its 0 cost when we reach the end or passed it
    #add the current cost and then the minimum of the future path recursively
    #choose between starting at index 0 or 1
        # def dfs(i):
        #     if i >=n:
        #         return 0 
        #     return cost[i] + min(dfs(i+1),dfs(i+2))
        # return min(dfs(0),dfs(1))

    #top down approach, recursively find the best path
    #record the best path at every index

        cache = [-1]*len(cost)

        def dfs(i):
            #base case, when surpassed, no further cost is required
            if i > len(cost)-1:
                return 0 
            
            #if the current one is computed, simply retrieve it
            if cache[i] != -1:
                return cache[i]
            #store the cost for this index
            cache[i] = cost[i] + min(dfs(i+1),dfs(i+2))
            return cache[i]
        return min(dfs(0),dfs(1))

            