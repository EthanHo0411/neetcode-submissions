class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #use dynamic programming, iterature through the array and decide an item is included or not
        
        #first make sure that the total sum is even number
        target = sum(nums)
        if target%2 != 0:
            return False
        target =  target //2
        #cache the results for each index and each num within the range of target
        cache = [[-1]*(target+1)  for i in range(len(nums))]

        def dfs(i, amount):
            if amount == 0:
                return True
            #make sure that it doesn't go out of bound and be exact
            if i>= len(nums) or amount <0:
                return False
            if cache[i][amount] != -1:
                return cache[i][amount]
            
            cache[i][amount] = dfs(i+1,amount-nums[i]) or dfs(i+1, amount)

            return cache[i][amount]
        return dfs(0,target)
            

            