class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        num = row*col
        l = 0
        r = num - 1
        while l <= r:
            mid = (l + r) // 2
            row_num = mid // col
            col_num = mid % col
            if matrix[row_num][col_num] == target:
                return True
            elif matrix[row_num][col_num] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
                