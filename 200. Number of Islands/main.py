class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        if not grid:
            return 0
        
        island_count  = 0
        n = len(grid)
        m = len(grid[0])
        
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j] == '1':
                    island_count += 1
                    # Change to water all the land of the island
                    self.changeToZeros(grid,i,j,n-1,m-1)

        return island_count

    def changeToZeros(self,grid: list[list[str]],i:int,j:int,n:int,m:int):
        if i < 0 or j < 0 or i > n or j > m or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        
        self.changeToZeros(grid,i-1,j,n,m)
        self.changeToZeros(grid,i,j+1,n,m)
        self.changeToZeros(grid,i+1,j,n,m)
        self.changeToZeros(grid,i,j-1,n,m)




# Test cases
s = Solution()
print(s.numIslands([["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"]])) # Expected 1

print(s.numIslands([["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]])) # Expected 3