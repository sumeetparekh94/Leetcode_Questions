class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if not m or not n:
            return 0

        dp = [[1 for i in range(m)] for j in range(n)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
