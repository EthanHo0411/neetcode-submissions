class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer approach from both ends
        #the formula for area is min height times the diff in index
        #move the min height pointer every time to explore larger heights 
        p1 = 0
        p2 = len(heights)-1
        max_water = 0 

        while p1<p2:
            min_height = min(heights[p1], heights[p2])
            water = (p2-p1)*min_height
            if water > max_water:
                max_water = water
            
            if heights[p1] == min_height:
                p1 += 1
            else:
                p2 -=1
        return max_water