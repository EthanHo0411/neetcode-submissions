class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums)-1

        while l < r:
            mid = l + ((r-l)//2)

            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid+1
        
        i = l
        l, r = 0 , len(nums)-1
        if nums[i] <= target <= nums[r]:
            l = i
        else:
            r = i
        
        while l <= r:
            mid = l + ((r-l)//2)

            if nums[mid] == target:
                return mid
            elif nums[mid]< target:
                l = mid +1 
            else:
                r = mid -1
        return -1
