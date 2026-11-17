class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array 
        #start from the left and choose the leftmost index as the target
        #choose two pointer: the immediate right of the index and the end of the list
        #the immediate right of the index becomes the left and the end becomes the right
        # calculate -nums[i] = nums[j] +nums[k]
        # perform the calculation until j surpasses k

        nums.sort()
        result = []

        #skip the last two as there would not be three number combo anyway
        for i in range(len(nums)-2):
            #if the current number i is already no zero positive, then no way there could be combo
            if nums[i] > 0:
                break
            
            #if the current number i is the same as the previous one,skip to prevent duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            #perform the 2sum search within the rest of the segment
            target = -nums[i]
            p1 = i+1
            p2 = len(nums)-1

            while p1<p2:
                number = nums[p1]+nums[p2]
                if target == number:
                    result.append([nums[i],nums[p1],nums[p2]])
                    p1+=1
                    p2-=1
                    #skip through the duplicated left pointers to prevent duplicates
                    while nums[p1] == nums[p1-1] and p1<p2:
                        p1+=1
                elif target > number:
                    p1+=1
                else:
                    p2-=1
        return result



            