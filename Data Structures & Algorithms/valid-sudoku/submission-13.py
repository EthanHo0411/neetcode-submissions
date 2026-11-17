class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # have three dictionary of sets, for each row, col and box 
        # place the value into the sets for checking 
        from collections import defaultdict 

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                item = board[row][col]

                #skip if the item is a dot 
                if item == ".":
                    continue

                #check if its a duplicate in its row 
                if item in rows[row]:
                    return False
                else:
                    rows[row].add(item)
                
                #check if its a duplicate in its col
                if item in cols[col]:
                    return False
                else: 
                    cols[col].add(item)
                
                #check if its a duplicate in its box
                box = (row//3)*3 + col//3
                if item in boxes[box]:
                    return False
                else: 
                    boxes[box].add(item)
        return True
