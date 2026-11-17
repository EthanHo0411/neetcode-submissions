class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)
        def dfs(i):
            #base case
            if i >len(nums)-1:
                return 0
            
            #if we have alreayd seen the profit starting from this index, then simply return
            if cache[i] != -1:
                return cache[i]
            
            #we choose to rob or not to rob
            cache[i] = max(nums[i]+dfs(i+2), dfs(i+1))
            return cache[i]
        return dfs(0)