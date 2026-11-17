class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       from collections import defaultdict
       dicct = defaultdict(int)
       for num in nums:
        if dicct[num] == 1:
            return True
        else:
            dicct[num] = 1
       return False
