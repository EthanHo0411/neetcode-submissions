class Solution:
    def findMin(self, nums: List[int]) -> int:
        #do binary space searh
        l,r = 0 , len(nums)-1

        while l < r:
            mid = l + ((r-l)//2)
            num = nums[mid]
            #when only the mid and right is the same segment, then the min is on the left
            if num<nums[r]:
                r = mid
            #when only num and left is the same segment , then the min is on the right part
            else:
                l = mid+1
        return nums[l]          
            