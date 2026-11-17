class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #since there must be a pair of result
        #when we see a newnumber , store it in the hashmap 
        #when we come across another number that have the target-number equal to one of the stored number
        #we know that we have found the pair

        from collections import defaultdict
        dictt = defaultdict(int)

        for i, num in enumerate(nums):
            remain = target - num
            if remain in dictt:
                return [dictt[remain], i]
            dictt[num] = i
            
        