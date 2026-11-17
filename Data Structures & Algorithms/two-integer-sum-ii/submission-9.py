class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since its in non decreasing order ,we can tune the pair of number by moving the left and right pointer
        p1 = 0
        p2 = len(numbers)-1
        while p1 < p2:
            num = numbers[p1]+numbers[p2]
            if num>target:
                p2-=1
            elif num< target:
                p1+=1
            else:
                return [p1+1,p2+1]
