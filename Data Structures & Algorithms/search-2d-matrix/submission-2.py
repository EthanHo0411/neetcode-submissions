class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first do binary search on the rows to identify the row
        #then do binary search on the cols to identify the col

        #first do binary search on the rows to identify the row
        #optimise: check the first and last element of the row 
        #check if the target is within the row , if not , shift the pointers
        l,r = 0 , len(matrix)-1
        target_row = 0 
        while l <=r :
            mid = l + ((r-l)//2)
            head = matrix[mid][0]
            tail = matrix[mid][-1]
            if head <= target <= tail:
                target_row = mid
                break
            elif target > tail:
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



