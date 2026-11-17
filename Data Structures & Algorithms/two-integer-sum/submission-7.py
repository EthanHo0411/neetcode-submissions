class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #since we know that must exist one pair of number that equals the target
        #the intuition is that if one number is part of this desired pair
        #then its diff between the target would also be present in the list
        #we use a hashmap to keep track of the number we have seen
        #first we use enumerate function to get the index and the value of the list
        #then calculate the diff between the target and this number
        #if the diff is present in our hashmap , it implies the current number and the diff is the pair we want
        #return its index
        #otherwise , store the current number in the hashmap for later checking


        prevMap = {}  # val -> inde
        for i ,x in enumerate(nums):
            diff = target - x
            if diff in prevMap:
                return [prevMap[diff], i ]
            prevMap[x] = i 