class Solution:
    def trap(self, height: List[int]) -> int:
        #the idea is to process water trapped individually at each index
        #property : amount of rain water determined by the min of both side 
        #progress with the side with min height 
        #have a max l and max r height for comparison 
        i ,j = 0 , len(height)-1

        maxl, maxr = height[i], height[j]
        area = 0

        while i <= j:
            if maxl < maxr: 
                maxl = max( maxl, height[i])
                area += maxl-height[i]
                i+=1
            else:
                maxr = max( maxr, height[j])
                area += maxr-height[j]
                j-=1
        return area
            
