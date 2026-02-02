class Solution:
    def visit_cell(self, i, j, size):
        if i < 0 or i>size[0] or j<0 or j>size[1] or self.grid[i][j] == "0":
            return 

        self.grid[i][j] = "0"
        self.visit_cell(i+1, j, size)
        self.visit_cell(i, j+1, size)
        self.visit_cell(i-1, j, size)
        self.visit_cell(i, j-1, size)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] != "0":
                    self.visit_cell(i, j, (len(grid) - 1, len(grid[0]) - 1))
                    answer += 1
        return answer