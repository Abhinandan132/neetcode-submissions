class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0]) 
        # Initialize a sum matrix (prefix) 
        """Initialize a prefix matrix padded by 0's to find above sum. 
        0 0 0 0
        0 1 1 0
        0 2 3 0
        0 0 0 0 eg. """
        self.prefix_mat = [[0] * (cols + 1) for row in range(rows + 1)]
        # Finding the prefix sum (Row wise)
        for r in range(rows): 
            prefix = 0 
            for c in range(cols): 
                prefix += matrix[r][c]  
                # Offset due to 0 pad
                self.prefix_mat[r + 1][c + 1] = prefix + self.prefix_mat[r][c + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1 # Add due to padding
        bottom_right = self.prefix_mat[r2][c2] # Whole square. 
        above = self.prefix_mat[r1 - 1][c2] 
        left = self.prefix_mat[r2][c1 - 1]
        top_left = self.prefix_mat[r1 - 1][c1 - 1] 
        return bottom_right - above - left + top_left
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)