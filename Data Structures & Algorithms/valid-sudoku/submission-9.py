class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #use a three dictionary approach , one dictionary for each component
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        #go through individual block and check if its inside
        for row in range(9):
            for col in range(9):
                item = board[row][col]
                if item == ".":
                    continue
                boxnum = (row//3)*3 + col//3
                if (item in rows[row] or item in cols[col] or item in boxes[boxnum]):
                    return False
                else:
                    rows[row].add(item)
                    cols[col].add(item)
                    boxes[boxnum].add(item)
        return True

