class Solution:
    def trap(self, height: List[int]) -> int:
        #the idea is to process water trapped individually at each index
        #property : amount of rain water determined by the min of both side 
        #progress with the side with min height 
        #have a max l and max r height for comparison 

        i = 0
        j = len(height)-1
        while i < j and height[i] == 0:
            i+=1
        while j> 0 and height[j] == 0:
            j-=1

        maxl = height[i]
        maxr = height[j]
        
        total = 0 
        while i <= j:
            if maxl < maxr:
                maxl = max(maxl, height[i])
                total += maxl - height[i]
                i +=1 
            else: 
                maxr = max(maxr, height[j])
                total += maxr - height[j]
                j-=1
        return total 
