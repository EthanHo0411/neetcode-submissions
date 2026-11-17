class Solution:
    def jump(self, nums: List[int]) -> int:
        #dp top down
        cache = {}

        def dfs(i):
            #if we can jump to or past, then the base case is 0
            if i >= len(nums)-1:
                return 0
            
            #if the index is computed already, its in the cache ,return directly
            if i in cache:
                return cache[i]
            
            #if the current nums[i]is 0 we cnt jump from this location
            if nums[i] == 0:
                return -1
            
            #recurrence, determine the min no.of jumps by looking at the future jumpable ones
            cache[i] = min([1+dfs(i+j) if dfs(i+j) != -1 else float("inf") for j in range(1,nums[i]+1)])

            return cache[i]
        return dfs(0)