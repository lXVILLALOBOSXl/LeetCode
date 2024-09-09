class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n < 1 or m < 1:
            return 0
        
        rows, cols = m, n
        sum = 1

        dp = [[None for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j - 1]

        return dp[rows - 1][cols - 1]

# Test cases
s = Solution()
print(s.uniquePaths(3,7)) # Expected 28
print(s.uniquePaths(3,2)) # Expected 3
print(s.uniquePaths(7,3)) # Expected 28
print(s.uniquePaths(3,3)) # Expected 6
print(s.uniquePaths(1,1)) # Expected 1