class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #first we initialise a set which we would use to store the numbers
        #the set allows for O(1) access to elements to check for their existence
        #for every number we see , we add them to the set
        #if the number is already in the set , it implies theres a duplicate
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False