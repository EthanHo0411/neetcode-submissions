class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #sliding window approach, at each pair of index record the area
        #move the pointer with the smaller height so as to further increase the height

        i = 0
        j = len(heights)-1
        maxarea = 0 
        while i < j:
            area = min(heights[i], heights[j])*(j-i)
            maxarea = max(area, maxarea)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return maxarea