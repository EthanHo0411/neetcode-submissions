class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #sliding window approach, at each pair of index record the area
        #move the pointer with the smaller height so as to further increase the height
        l, r = 0 , len(heights)-1
        maxarea = float("-inf")
        while l < r:

            height = min(heights[l], heights[r])
            length = r - l 
            area = height*length

            maxarea = max(maxarea , area)
            if heights[l] > heights[r]:
                 r-=1
            else: 
                l+=1
        return maxarea
