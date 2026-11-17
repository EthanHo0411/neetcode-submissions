class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #the area to contain water is equal to the rectangle created by min height and the distance of the rods
        #skip any zero height bar at the start
        #each time calculat the area and then move the bar with the lowest height to a new one
        #this makes sure that the area can be larger

        l = 0
        r = len(heights)-1
        while heights[l] == 0 :
            l+=1
        while heights[r] == 0:
            r -=1
        
        maxarea = 0 
        while l<r:
            width = r-l
            height = min(heights[l],heights[r])
            area = width*height
            maxarea = max(area,maxarea)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxarea
