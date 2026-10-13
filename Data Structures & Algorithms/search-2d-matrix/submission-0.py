class Solution: 
    def search_row(self, matrix, target): 
        l, h = 0, len(matrix) - 1
        while(l <= h): 
            mid = (l + h)//2; 
            if (matrix[mid][0] <= target <= matrix[mid][len(matrix[0]) - 1]): 
                return mid 
            elif (matrix[mid][0] > target): h = mid - 1
            else: l = mid + 1
        return -1 
    
    def search_in_row(self, row, target): 
        l, h = 0, len(row) - 1
        while(l <= h): 
            mid = (l + h)//2; 
            if (row[mid] == target): return True 
            elif (row[mid] <target): l = mid + 1
            else: h = mid - 1
        return False 

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # All the rows are non over apping. 
        # Find potential row, then in that row.  
        row = self.search_row(matrix, target)
        if (row) == -1: return False 
        return self.search_in_row(matrix[row], target)
    