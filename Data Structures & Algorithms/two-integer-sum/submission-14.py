class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #store each number upon meeting
        #check if target - current number is present 
        #return the corresponding pair of index
        seen = {}
        for i in range(len(nums)):
            result = target - nums[i]

            if result in seen: 
                return [seen[result], i ]

            seen[nums[i]] = i
        