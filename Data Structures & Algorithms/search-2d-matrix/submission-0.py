class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        top, bottom = 0, m-1

        while top <= bottom:
            mid_level = (top + bottom) // 2

            if matrix[mid_level][0] > target:
                bottom = mid_level - 1
            elif matrix[mid_level][0] < target:
                top = mid_level + 1
            else:
                return True
        
        l, r = 0, n - 1

        while l <= r:
            mid = (l+r) // 2

            if matrix[bottom][mid] == target:
                return True
            elif matrix[bottom][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False            