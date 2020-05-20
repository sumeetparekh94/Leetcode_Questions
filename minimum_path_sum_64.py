class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        temp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        sum_ = 0

        for i in range(len(grid[0])):
            temp[0][i] = sum_ + grid[0][i]
            sum_ = temp[0][i]

        sum_ = 0
        for i in range(len(grid)):
            temp[i][0] = sum_ + grid[i][0]
            sum_ = temp[i][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                temp[i][j] = min(temp[i - 1][j], temp[i][j - 1]) + grid[i][j]

        return temp[-1][-1]

