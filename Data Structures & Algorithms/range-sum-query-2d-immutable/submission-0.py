class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.cum = [[0] * (COLS + 1) for c in range(ROWS + 1)]
        print(self.cum)

        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                self.cum[i][j] = self.cum[i-1][j] + self.cum[i][j-1] + matrix[i-1][j-1] - self.cum[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1; col1 += 1; row2 += 1; col2 += 1

        full = self.cum[row2][col2]
        top = self.cum[row1-1][col2]
        left = self.cum[row2][col1-1]
        top_left = self.cum[row1-1][col1-1]

        return full - top - left + top_left



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)