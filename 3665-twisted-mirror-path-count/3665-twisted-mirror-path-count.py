class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        n = len(grid[0])

        dp = [0] * n
        dp[0] = 1

        for row in grid:
            left = 0

            for j in range(n):
                if row[j] == 1:
                    left, dp[j] = dp[j], left
                else:
                    left = (left + dp[j]) % MOD
                    dp[j] = left

        return left