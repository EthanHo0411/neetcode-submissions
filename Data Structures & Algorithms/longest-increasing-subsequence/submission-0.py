class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # initialise to 1 for each index
        result =  [1 for x in nums]

        #sort the array so its strictly increasing
        #subproblem is choosing the longest sequence from previous index
        #the previous index holds number smaller than the current index
        #and the previous index has to be smaller than the current index

        nums = nums.copy()

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            result[i] = max([result[j] for j in range(i) if nums[j]<nums[i]]+[0])+1
        return max(result)
