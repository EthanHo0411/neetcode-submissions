class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #search vertically for the correct row
        l = 0
        r = len(matrix)-1
        rowNumber = -1
        while l<=r:
            mid = l + ((r-l)//2)
            rowFirstItem = matrix[mid][0]
            rowLastItem = matrix[mid][-1]
            #check if the target is within the range of that row
            if rowFirstItem <= target <= rowLastItem:
                rowNumber = mid
                break
            elif target > rowFirstItem:
                l = mid+1
            else:
                r = mid-1
        if rowNumber == -1:
            return False
        #search horizontally for the correct number
        l = 0
        r = len(matrix[0])-1
        row = matrix[rowNumber]
        while l<=r:
            mid = l + ((r-l)//2)
            item = row[mid]
            if item == target:
                return True
            elif target > item:
                l = mid+1
            else:
                r = mid - 1
        return False

