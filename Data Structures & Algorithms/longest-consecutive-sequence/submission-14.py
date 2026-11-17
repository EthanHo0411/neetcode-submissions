class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #identify the start of a consecutive list 
        #if the number doesn't have a number smaller than it, its a start
        #check the length of these possible start 

        maxlen = float("-inf")
        numbers = set(nums)
        for num in nums:
            if not num - 1 in numbers:
                length = 1
                temp = num 
                while temp+1 in numbers: 
                    length +=1 
                    temp +=1
                maxlen = max(maxlen , length)
        return maxlen if nums else 0