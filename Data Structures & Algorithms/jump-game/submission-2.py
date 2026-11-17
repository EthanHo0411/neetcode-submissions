class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #use dp with top down
        #from the end , check at each index if we can reach the end
        #at each index, we check the possibility of success of jumping to each index possible

        cache = {len(nums)-1: True}

        def dfs(i):

            if i >= len(nums)-1:
                return True
            if i in cache:
                return cache[i]
            
            #impossible to jump if nums[i] is 0
            if nums[i] == 0:
                cache[i] = False
                return False
            #recurrence
            cache[i] = any([ dfs(i+j)  for j in range(1,nums[i]+1)])
            return cache[i]
        return dfs(0)