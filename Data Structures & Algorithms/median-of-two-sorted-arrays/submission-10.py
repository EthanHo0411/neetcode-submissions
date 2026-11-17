class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #select a point that would divide the smaller array into two partition
        #calculate the number of elements needed in the bigger array so that
        #the left partition of the smaller array plus this number would be half of the elements
        #calculate this index in the big array that satisify this with j = (m+n)//2 - x
        #check if the maxleft small < min right big and max left big < min right small
        #if they satisfy , it means the current point choosen can be used as the median
        # if not then shift the binary search to choose other points


        #make sure that nums1 is the smaller array
        if len(nums1)>len(nums2):
            nums1 , nums2 = nums2, nums1

        m , n = len(nums1), len(nums2)
        l , r = 0 , m

        while l<=r:
            #choose the mid point in the smaller array
            mid = l + ((r-l)//2)
            #the max left small is the left of mid
            maxl1 = nums1[mid-1] if mid >0 else float("-inf")
            #the min right small is the mid
            minr1 = nums1[mid] if mid < m else float("inf")
            #calculate the number of elements needed in the big array, also the index
            j = (m+n+1)//2 - mid 

            #the max left big is the left of j
            maxl2 = nums2[j-1] if j > 0 else float("-inf")
            #the min right big is the j
            minr2 = nums2[j] if j <n else float("inf")

            if maxl1 <= minr2 and maxl2 <= minr1:
                if (m+n) %2 == 0:
                    return (max(maxl1,maxl2)+ min(minr1,minr2))/2
                else:
                    return max(maxl2,maxl1)
            elif maxl1 > minr2:
                r = mid -1
            else:
                l = mid+1
    

                    

