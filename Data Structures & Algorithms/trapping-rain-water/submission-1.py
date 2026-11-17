class Solution:
    def trap(self, height: List[int]) -> int:
        #first skip through the columns until a nonzero one appear (dont count the sides)
        #set the pointer to be at that index
        #iterate through the indexes and record their height
        #keep looping until a height same or higher than the value at the pointer appears
        #calculate the area with min height times diff in index
        #area = calculated - recorded aread( the one with blocks)
        #update the max area if needed

        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res