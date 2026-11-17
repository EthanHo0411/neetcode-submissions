class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        #sort the list and loop through the list 
        nums.sort()

        #index item = - ( sum of the other term )
        i = 0 
        while i < len(nums)-2:
            #if the index number is already positive theres no more combination
            if nums[i] > 0:
                break 
            
            #if the current number is the same as the previous then skip 
            if i > 0 and nums[i] == nums[i-1]:
                i +=1 
                continue 

            #turns it into a 2sum problem at each index of the list             
            target = -nums[i]
            j = i+1 
            k = len(nums)-1
            while j < k:
                total = nums[j]+nums[k]
                if total > target:
                    k-=1
                elif total < target:
                    j+=1
                else: 
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j< k and nums[j-1] == nums[j]:
                        j+=1
            i+=1
        return result

