class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for row in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[row][i] == ".":
        #             continue
        #         if board[row][i] in seen:
        #             return False
        #         seen.add(board[row][i])

        # for col in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[i][col] == ".":
        #             continue
        #         if board[i][col] in seen:
        #             return False
        #         seen.add(board[i][col])

        # for square in range(9):
        #     seen = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = (square//3) * 3 + i
        #             col = (square % 3) * 3 + j
        #             if board[row][col] == ".":
        #                 continue
        #             if board[row][col] in seen:
        #                 return False
        #             seen.add(board[row][col])
        # return True
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        for row in range(9): 
            for col in range(9): 
                sq_index = (row//3, col//3)
                val = board[row][col]
                if (val == '.'): continue 
                if (val in rows[row]) or (val in cols[col] or (val in squares[sq_index])): return False 
                rows[row].add(val)
                cols[col].add(val) 
                squares[sq_index].add(val)
        return True