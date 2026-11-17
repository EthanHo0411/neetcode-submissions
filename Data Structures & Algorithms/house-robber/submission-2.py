class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)

        def dfs(i):
            #base case
            #if it reaches the end of the list theres nth to steal
            if i >= len(nums):
                return 0
            #retrieve cached result
            if cache[i] != -1:
                return cache[i]

            cache[i] = max(nums[i]+ dfs(i+2),dfs(i+1))
            return cache[i]
        return dfs(0)