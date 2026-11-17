class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #use a stack approach where the stack exapnds when >= height histograms is seen
        #pop elements off the stack when the current histogram is < the top item
        #stack stores the index and the height of the object
        #area is calculared upon being popped

        from collections import deque 
        heights.append(0)
        stack = deque()
        maxarea = 0
        for i , height in enumerate(heights):
            index = i
            while stack and height < stack[-1][1]:
                item = stack.pop()
                index = item[0]
                heightt = item[1]
                area = (i-index)*heightt
                maxarea = max(maxarea, area)
            #append the index of the last item being popped
            #this index represent the longest width obtained from current to last popped
            stack.append([index,height])
        return maxarea

