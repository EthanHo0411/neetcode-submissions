class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #compute the prefix array
        prefix = [1]
        product = 1
        for i in range(1,len(nums)):
            product *= nums[i-1]
            prefix.append(product)
        
        #compute the suffix array
        suffix = [1]
        product = 1
        for i in range(len(nums)-2,-1, -1):
            product *= nums[i+1]
            suffix.insert(0,product)

        #result is multiplying prefix and suffix
        result = []
        for x,y in zip(prefix, suffix):
            result.append(x*y)
        return result

