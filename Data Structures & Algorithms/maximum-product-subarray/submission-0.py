class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Uuse dynamic programming to iterate through the array
        #at each step , determine if we should multiiply or not by choosing the max one
        #bottom up approach with base case equals to 1
        #keep track of min and max to cover the cases for the negative numbers

        res = float("-inf")
        curMin , curMax = 1, 1

        for num in nums:
            #store the curMax for deciding the curMin
            temp = curMax*num
            #considering the fact that negative could be inverted
            curMax = max(num, curMax*num, curMin*num)
            #find the curMin
            curMin = min(temp, curMin*num, num)
            res = max(res, curMax)
        return res