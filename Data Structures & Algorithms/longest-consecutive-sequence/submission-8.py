class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #the idea is that when a number dont have an entry that's 1 less than it
        #then it is the start of a sequence, which could be a potential longest sequence
        seqlen = 0
        numbers = set(nums)
        for num in nums:
            if num -1 not in numbers:
                templen = 1
                while num+1 in numbers:
                    templen +=1
                    num +=1
                seqlen = max(seqlen, templen)
        return seqlen