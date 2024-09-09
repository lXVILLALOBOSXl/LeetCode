from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        
        max_area = 0
        n= len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = self.count_area(grid,i,j,n-1,m-1)
                    max_area = area if (area > max_area) else max_area

        
        return max_area
    
    def count_area(self, grid: List[List[int]],i: int, j: int, n: int, m: int) -> int:
        if i < 0 or j < 0 or i > n or j > m or grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0

        up = self.count_area(grid,i-1,j,n,m) # Up
        right = self.count_area(grid,i,j+1,n,m) # Right
        down = self.count_area(grid,i+1,j,n,m) # Down
        left = self.count_area(grid,i,j-1,n,m) # Left

        return up + right + down + left + 1

# Test Cases 
s = Solution()
print(s.maxAreaOfIsland([[0,0,0,0,0,0,0,0]])) # Expected 0
print(s.maxAreaOfIsland([[1,1,1,1,1,1,1,1]])) # Expected 8
print(s.maxAreaOfIsland([[1,0,1,0,1,0,1,0]])) # Expected 1
print(s.maxAreaOfIsland([[1,0,1,1,1,0,1,0]])) # Expected 3
print(s.maxAreaOfIsland([[1,0,1,1,1,0,1,0],
                         [1,0,1,1,1,0,1,0]])) # Expected 6
print(s.maxAreaOfIsland([[1,0,1,1,1,0,1,0],
                         [1,0,1,1,1,0,1,0],
                         [1,0,1,1,1,0,1,0]])) # Expected 9
print(s.maxAreaOfIsland(None)) # Expected 0
print(s.maxAreaOfIsland([])) # Expected 0
print(s.maxAreaOfIsland([[]])) # Expected 0
print(s.maxAreaOfIsland([[0]])) # Expected 0
print(s.maxAreaOfIsland([[1]])) # Expected 1
print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                          [0,0,0,0,0,0,0,1,1,1,0,0,0],
                          [0,1,1,0,1,0,0,0,0,0,0,0,0],
                          [0,1,0,0,1,1,0,0,1,0,1,0,0],
                          [0,1,0,0,1,1,0,0,1,1,1,0,0],
                          [0,0,0,0,0,0,0,0,0,0,1,0,0],
                          [0,0,0,0,0,0,0,1,1,1,0,0,0],
                          [0,0,0,0,0,0,0,1,1,0,0,0,0]])) # Expected 6