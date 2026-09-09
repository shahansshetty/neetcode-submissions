class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row
        for row in range(9):
            seen=set()
            for i in range(9):
                if board[row][i]=='.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])        
        #column
        for column in range(9):
            seen=set()
            for i in range(9):
                if board[i][column]=='.':
                    continue
                if board[i][column] in seen:
                    return False
                seen.add(board[i][column])    

        #3*3 box
        for square in range(9):
            seen=set()
            for i in range(3):
                for j in range(3):
                    row=(square//3)*3+i
                    column=(square%3)*3+j
                    if board[row][column]=='.':
                        continue
                    if board[row][column] in seen:
                        return False
                    seen.add(board[row][column])


        return True  