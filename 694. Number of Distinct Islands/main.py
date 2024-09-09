
class Solution:
    def numOfDistinctIslands(self, grid: list[list[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        
        islands = set()
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islands.add(self.getIsland(grid,i,j,n-1,m-1,'X'))

        return len(islands)



    def getIsland(self,grid: list[list[str]],i:int,j:int,n:int,m:int,pos:str) -> str:
        if i < 0 or j < 0 or i > n or j > m or grid[i][j] == '0':
            return 'O'
        
        # X = Start
        # O = Out of bounds or 0
        # U = Up
        # R = Right 
        # L = Left
        # D = Down

        grid[i][j] = '0'

        up = self.getIsland(grid,i-1,j,n,m,"U")
        right = self.getIsland(grid,i,j+1,n,m,"R")
        down = self.getIsland(grid,i+1,j,n,m,"D")
        left =  self.getIsland(grid,i,j-1,n,m,"L")

        return pos + up + right + down + left

        
        


# Test cases
s = Solution()

# Expected 3
print(s.numOfDistinctIslands([      ["1","1","0","1","1"],
                                    ["1","0","0","0","0"],
                                    ["0","0","0","0","1"],
                                    ["1","1","0","1","1"]]))

# Expected 0
print(s.numOfDistinctIslands([["0","0","0","0","0"],
                              ["0","0","0","0","0"],
                              ["0","0","0","0","0"],
                              ["0","0","0","0","0"]]))

# Expected 1
print(s.numOfDistinctIslands([["1","1","1","1","1"],
                              ["1","1","1","1","1"],
                              ["1","1","1","1","1"],
                              ["1","1","1","1","1"]]))

# Expected 2
print(s.numOfDistinctIslands([["1","1","1","1","0"],
                              ["1","0","0","0","0"],
                              ["0","0","0","0","1"],
                              ["1","1","1","1","1"]]))

# Expected 0
print(s.numOfDistinctIslands(None))

print(s.numOfDistinctIslands([["1","1","1","0","1"]]))