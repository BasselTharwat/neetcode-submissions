class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        l = 0
        m = 0
        while l < 9:
            m = 0
            while m < 9:
                oneToNine = set(["1","2","3","4","5","6","7","8","9"])
                for i in range(3):
                    for j in range(3):
                        print("oneToNine: ", oneToNine)
                        print("curr: ", board[l + i][m + j])
                        if board[l + i][m + j] != "." and board[l + i][m + j] not in oneToNine:
                            return False
                        else:
                            oneToNine.discard(board[l + i][m + j]) 
                m += 3
            l += 3
        
        for i in range(9):
            row = board[i]
            oneToNine = set(["1","2","3","4","5","6","7","8","9"])
            for j in range(9):
                if row[j] != "." and row[j] not in oneToNine:
                    return False
                else:
                    oneToNine.discard(row[j])

        for i in range(9):
            oneToNine = set(["1","2","3","4","5","6","7","8","9"])
            for j in range(9):
                if board[j][i] != "." and board[j][i] not in oneToNine:
                    return False
                else:
                    oneToNine.discard(board[j][i])

        


        return True
        