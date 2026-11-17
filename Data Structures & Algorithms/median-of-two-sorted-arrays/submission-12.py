class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #select a point that would divide the smaller array into two partition
        #calculate the number of elements needed in the bigger array so that
        #the left partition of the smaller array plus this number would be half of the elements
        #calculate this index in the big array that satisify this with j = (m+n+1)//2 - x
        #check if the maxleft small < min right big and max left big < min right small
        #if they satisfy , it means the current point choosen can be used as the median
        # if not then shift the binary search to choose other points

        #make sure that nums1 is the smaller array we are finding the index in
        if len(nums1)>len(nums2):
            nums1 ,nums2 = nums2 ,nums1

        #create left and right pointer
        #******the middle point is between two indexes, its not an index******
        m , n = len(nums1), len(nums2)
        l,r = 0 , m

        while l <= r:
            mid = l + ((r-l)//2)

            #figure out the maxl and minr of the current mid
            maxl1 = nums1[mid-1] if mid > 0 else float("-inf")
            minr1 = nums1[mid] if mid<m else float("inf")

            #figure out how many items in the big array has to be smaller than this current mid
            # find a mid index that would separate the big into left and right partition to suit this need

            #plus one makes odd number sum able to get more item on the left partition 
            #while maintaining the original number for even numbers
            #the mid index itself means deducting the elements before it 
            j = (m+n+1)//2 - mid

            maxl2 = nums2[j-1] if j>0 else float("-inf") 
            minr2 = nums2[j] if j<n else float("inf")

            #make sure that this mid index is also the mid index for both array
            if maxl1 <=minr2 and maxl2<=minr1:
                if (m+n) %2 == 0:
                    return (max(maxl1, maxl2) + min(minr2,minr1))/2
                else:
                    return max(maxl2,maxl1)
            elif maxl1 > minr2:
                r = mid -1 
            else:
                l = mid+1
        


