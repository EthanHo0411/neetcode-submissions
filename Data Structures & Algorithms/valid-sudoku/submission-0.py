class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check if the component has the right values and amount
        def check_valid(dictt):
            # Skip the "." entries
            if "." in dictt:
                del dictt["."]
            
            # Check if all present numbers are valid (1-9)
            for key in dictt.keys():
                # Convert string digits to integers for comparison
                try:
                    num = int(key)
                    # Check if the number is in valid range
                    if num < 1 or num > 9:
                        return False
                except ValueError:
                    # If key isn't "." or a valid number
                    return False
            
            # Check for duplicates (any number appearing more than once)
            for value in dictt.values():
                if value > 1:
                    return False
            
            return True
        
        #produce a dict from an array
        def populate_dict(array):
            dictt = {}
            for x in array:
                if x in dictt:
                    dictt[x]+=1
                else:
                    dictt[x] =1
            return dictt

        #check for the rows
        for row in board:
            if not check_valid(populate_dict(row)):
                return False
        
        #check the col
        for col in range(9):
            vertical_component = []
            for row in range(9):
                vertical_component.append(board[row][col])
            if not check_valid(populate_dict(vertical_component)):
                return False
        
        #create 9 boxes to store entries
        boxes = [[] for x in range(9)]
        #check the boxes
        for row in range(9):
            for col in range(9):
                box_index = (row//3)*3 + (col//3)
                boxes[box_index].append(board[row][col])
        
        #check if each box is valid
        for box in boxes:
            if not check_valid(populate_dict(box)):
                return False
        return True

        