class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #to make sure a sudoku is valid, check each row, col and box

        #use a helper function for check each component (get hashamp as input and boolean as output)
        #it ignores the dots, and check if the hashamp contains string other than 1 to 9
        #then it make sure the frequency of 1 to 9 appearence is at most 1

        #use a helper function to convert the component list into hashmap for frequency checking

        #first check the row, there are len(board) number of rows
        #secondly check the col, there are len(board[0]) numeber of cols (for col in cols and for row in rows)
        #lastly check the boxes
        #create a boxes list with 9 sublist containing items for each box
        # loop through each item on the board and calculate their corresponding box
        # with this formual box_index = (row//3)*3 + (col//3)
        #this would populate the boxes list
        #then check individual box in the list
        #time complexity O(n^2)

        #check if the component has the right values and amount
        def check_valid(dictt):
            #skips the "." entries:
            if "." in dictt:
                del dictt["."]

            #make sure the entries are only integer from 1 to 9
            for key in dictt.keys():
                try:
                    num = int(key)
                    if not(1<=num<=9):
                        return False
                except ValueError:
                        return False
            #make sure the requency is 1
            for key in dictt.keys():
                if dictt[key] >1:
                    return False
            return True
        
        #produce a dict from an array
        def populate_dict(array):
            dictt = {}
            for x in array:
                dictt[x] = dictt.get(x,0)+1
            return dictt

        #check for the rows:
        for row in board:
            if not check_valid(populate_dict(row)):
                return False
        
        #check for columns
        for col in range(9):
            vertical = []
            for row in range(9):
                vertical.append(board[row][col])
            if not check_valid(populate_dict(vertical)):
                return False
        
        
        #create 9 boxes to store entries
        boxes = [[] for x in range(9)]
        #check the boxes
        for row in range(9):
            for col in range(9):
                box_index = (row//3)*3 + col//3
                boxes[box_index].append(board[row][col])
        
        #check if each box is valid
        for box in boxes:
            if not check_valid(populate_dict(box)):
                return False
        return True

        