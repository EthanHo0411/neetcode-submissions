class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #use a stack approach where the stack exapnds when >= height histograms is seen
        #pop elements off the stack when the current histogram is < the top item
        #stack stores the index and the height of the object
        #area is calculared upon being popped

        from collections import deque 
        heights = heights.copy()
        heights.append(float("-inf"))
        stack = deque()
        maxarea = float("-inf")
        for i , height in enumerate(heights):
            index = i
            while stack and height < stack[-1][1]:
                item = stack.pop()
                index = item[0]
                heightt = item[1]
                area = (i-index)*heightt
                maxarea = max(maxarea, area)
            stack.append([index,height])
        #sequence in strict increasing order left
        return maxarea

