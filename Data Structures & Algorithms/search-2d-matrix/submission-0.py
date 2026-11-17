class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first do binary search on the rows to identify the row
        #then do binary search on the cols to identify the col

        l,r = 0 , len(matrix)-1
        target_row = 0 
        while l <=r :
            mid = l + ((r-l)//2)
            item = matrix[mid][0]
            item1 = matrix[mid][-1]
            up = matrix[mid+1][0] if mid != len(matrix)-1 else None
            down = matrix[mid-1][-1] if mid != 0 else None

            if (down and down<target<=item1) or (up and up>target>=item):
                target_row = mid
                break
            elif target > item:
                l = mid+1
            else:
                r = mid-1

        l,r = 0 , len(matrix[0])-1
        while l <= r:
            mid = l + ((r-l)//2)
            if target == matrix[target_row][mid]:
                return True
            elif target < matrix[target_row][mid]:
                r = mid-1
            else:
                l = mid+1
        return False 



