class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #backtracking 
        #have a result list and subset list for storing the numbers 
        res = []
        subset = []

        def dfs(i):
            #when reaching the end ,add the subset to the list
            if i>=len(nums):
                res.append(subset.copy())
                return 
            #addd the number to the subset
            subset.append(nums[i])
            #find the subset that include this number
            dfs(i+1)

            #pop it ,find the subset that doesnt include this number
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
            
