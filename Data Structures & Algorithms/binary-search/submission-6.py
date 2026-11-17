class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = l + ((r-l)//2)
            item = nums[mid]
            if item == target:
                return mid
            elif item<target:
                l = mid+1
            else:
                r = mid-1
        return -1
