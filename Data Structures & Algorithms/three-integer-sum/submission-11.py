class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #scan through the array one element at a time and perform 2sum search in the right part of the element
        #sort the array so that 2sum search can be done with pointers from both side
        #rearrange the equation to be nums[i] = nums[l]+nums[k]
        #this implies that as long as nums[i] is originally negative , there is a possible combination
        #if nums[i] >0 , then there is no way for l and r to be negative to sum the three into 0
        nums.sort()
        result = []
        #the main loop is used to loop through individual elements
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            
            if i >=1 and nums[i] == nums[i-1]:
                continue 
            
            target = -nums[i]

            #the secondary loop that scan through the right part of the array
            l = i+1
            r = len(nums)-1
            while l<r:
                right = nums[l]+nums[r]
                if  right == target:
                    result.append([-target, nums[l],nums[r]])
                    l+=1
                    while l< r and nums[l] == nums[l-1]:
                        l+=1
                elif right <target:
                    l+=1
                else:
                    r-=1
        return result


            