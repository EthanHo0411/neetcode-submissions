class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums)-1

        while l < r: 
            mid = (r-l)//2 + l
            # the min would always be in the right partition unless its original
            #when mid its at the right partition, we slowly shrink to the left , including mid
            if nums[mid] < nums[r]:
                r = mid 
            else: 
            # mid is not at the right partition yet
            # min would be at least at position mid +1 
                l = mid + 1
        return nums[l]



