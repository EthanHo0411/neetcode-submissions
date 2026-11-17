class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #store each number upon meeting
        #check if target - current number is present 
        #return the corresponding pair of index

        seen = {}

        for i , num in enumerate(nums):
            number = target - num
            if number in seen:
                return [seen[number], i]
            seen[num] = i

