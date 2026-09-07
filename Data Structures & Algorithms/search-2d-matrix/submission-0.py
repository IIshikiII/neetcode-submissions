class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x_len = len(matrix[0])
        y_len = len(matrix)
        matrix_len = x_len * y_len
        
        L = 0
        R = matrix_len - 1
        while L <=  R:
            mid = (L + R) // 2
            y = mid // x_len
            x = mid % x_len
            mid_val = matrix[y][x]
            if mid_val < target:
                L = mid + 1
            elif mid_val > target:
                R = mid - 1
            else:
                return True
        return False