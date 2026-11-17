class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #fist locate the row in which the target is located 
        l , r = 0 , len(matrix)-1
        row = 0
        while l <= r:
            mid = (r-l)//2 + l 
            topItem = matrix[mid][0]
            lastItem = matrix[mid][-1]

            if topItem <= target <= lastItem:
                row = mid 
                break
            elif target > lastItem: 
                l = mid + 1
            else:
                r = mid - 1
        #now locate the target within the prelcoated row 

        l, r = 0 , len(matrix[0])-1
        while l <= r: 
            mid = (r-l)//2 + l
            item = matrix[row][mid]

            if target == item: 
                return True 
            elif target > item: 
                l = mid + 1
            else:
                r = mid -1
        return False


