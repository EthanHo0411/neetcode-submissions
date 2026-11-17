class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #first use binary search to find the min value , the split of two partition 
        l , r = 0 , len(nums)-1

        while l < r: 
            mid = (r-l)//2 + l 

            if nums[mid] < nums[r]:
                r = mid 
            else: 
                l = mid + 1

        #figure out which part of the array its in
        i = l
        l , r = 0 , len(nums)-1
        if nums[i] <=  target <= nums[r]:
            l = i 
        else: 
            r = i - 1
        
        #do binary search for the target:
        while l<=r:
            mid = (r-l)//2 + l

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
        