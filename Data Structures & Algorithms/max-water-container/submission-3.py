class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer approach from both ends
        #the formula for area is min height times the diff in index
        #move the min height pointer every time to explore larger heights 
        maxarea = 0 
        l ,r = 0 , len(heights)-1
        while l<r:
            if heights[l] == 0:
                l+=1
                continue
            #calculate the currently bounded area
            area = (r-l)*min(heights[l],heights[r])
            maxarea = max(maxarea, area)

            #update the boundary by moving the pointer with smaller height
            #an increase in the height of the smaller bound can yield larger area
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxarea
            