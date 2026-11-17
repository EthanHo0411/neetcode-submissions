class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #the idea is to split the product into two passes
        #forward pass
        resultl = [1]
        for i in range(1,len(nums)):
            resultl.append(resultl[-1]*nums[i-1])
        #backward pass
        resultr = [1]
        for i in range(len(nums)-2, -1 , -1):
            resultr.insert(0, resultr[0]*nums[i+1])
        return list(map(lambda x : x[0]*x[1], zip(resultl,resultr)))