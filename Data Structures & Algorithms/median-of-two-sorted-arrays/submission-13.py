class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find the smaller array
        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2, nums1
        
        #define the index range for the number of nums1 item in the left partition
        import math 
        m = len(nums1)
        n = len(nums2)
        half = (m+n)//2
        #make sure the index is within range of nums1 
        l , r = 0 , m - 1

        #do binary search for the right index in nums1
        #condition on satisfying :  all items in left < right partition
        while True:
            mid = (r-l)//2 + l 
            #find out the number of item used in nums1 and determine the index to be used in nums2
            mid1 = half - (mid + 1) - 1

            l1 = nums1[mid] if mid >=0 else float("-inf")
            r1 = nums1[mid + 1] if mid + 1 <= m-1 else float("inf")
            l2 = nums2[mid1] if mid1 >= 0 else float("-inf")
            r2 = nums2[mid1+1] if mid1 +1 <= n-1 else float("inf")

            if l1 > r2:
                r = mid - 1
            elif l2 > r1:
                l = mid + 1
            else:
                #if the length is even 
                if (m+n) % 2 == 0: 
                    return (max(l1, l2) + min(r1, r2))/2
                #if the length is odd
                return min(r1, r2) 



