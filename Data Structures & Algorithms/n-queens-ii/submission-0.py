class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        board = [["."] * n for i in range(n)]
        
        def isSafe(r, c):
            row = r - 1
            while row >= 0:
                if board[row][c] == 'Q':
                    return False
                row -= 1
            
            row = r - 1
            col = c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1

            row = r - 1
            col = c + 1
            while row >= 0 and col < n:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col += 1

            return True
        

        def backtrack(r):
            if r == n:
                self.res += 1
                return
            
            for c in range(n):
                if isSafe(r, c):
                    board[r][c] = 'Q'
                    backtrack(r + 1)
                    board[r][c] = '.'
            
        backtrack(0)
            
        return self.res