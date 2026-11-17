class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #the product of every term except the item at index i can be separated into to portion
        #first portion is the product of elements before index i 
        #and then second portion is the product of elements after i
        #multiplying the two portion gives the desired product
        #the time complextiy is O(n) for two iterations

        #first portion
        prefix = [1]
        for i in range(1, len(nums)):
            num = prefix[-1]*nums[i-1]
            prefix.append(num)
        
        #second portion
        suffix = [1]
        for j in range(len(nums)-2, -1,-1):
            num = suffix[0]*nums[j+1]
            suffix.insert(0,num)
        result = []
        for x, y in zip(prefix, suffix):
            result.append(x*y)
        return result