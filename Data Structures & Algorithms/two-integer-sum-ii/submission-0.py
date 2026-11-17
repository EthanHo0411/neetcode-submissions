class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #one pointer at the start and one at the end
        #when the sum is > target then decrease end pointer
        #when the sum is < target then increase start  pointer

        p1 = 0
        p2 = len(numbers)-1
        while True:
            num = numbers[p1]+numbers[p2]
            if num < target:
                p1+=1
            elif num > target:
                p2-=1
            else:
                return [p1+1,p2+1]