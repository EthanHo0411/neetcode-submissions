class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array 
        #start from the left and choose the leftmost index as the target
        #choose two pointer: the immediate right of the index and the end of the list
        # calculate -nums[i] = nums[j] +nums[k]
        # perform the calculation until j surpasses k

        nums.sort()
        result = []
        for i in range(len(nums)-2):
            #if the number at i is positive then the formula wont hold
            if nums[i] >0:
                continue
            
            #prevent duplicates by skipping numbers of the same value
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            p1 = i+1
            p2 = len(nums)-1

            #while the pointers are not passing eachother
            while p1<p2:
                num = nums[p1]+nums[p2]
                if num == target:
                    result.append([nums[i],nums[p1],nums[p2]])
                    p1+=1
                    p2-=1
                    #prevent duplicates by skipping duplicating values
                    while nums[p1] == nums[p1-1]and p1<p2:
                        p1+=1
                elif num > target:
                    p2-=1
                else:
                    p1+=1
        return result