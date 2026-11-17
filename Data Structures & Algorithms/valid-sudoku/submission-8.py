class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        #use defauldict to get dictionary with int key and set values
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                item = board[row][col]
                if item == ".":
                    continue
                #if the item appeared in one of the set
                #it is duplicated and thus invalid
                if(item in rows[row] or 
                   item in cols[col] or
                   item in boxes[(row//3)*3 + col//3] ):
                   return False
                #record the item in the component sets
                rows[row].add(item)
                cols[col].add(item)
                boxes[(row//3)*3 + col//3].add(item)
        return True