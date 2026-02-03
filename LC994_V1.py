class Solution:
    def rotOranges(self, i, j, itr):

        if i < 0 or j < 0 or i >= self.m or j >= self.n or self.grid[i][j] == 0 or itr > self.answer[i][j]:
            return

        self.answer[i][j] = itr
        self.rotOranges(i+1, j, itr+1)
        self.rotOranges(i, j+1, itr+1)
        self.rotOranges(i-1, j, itr+1)
        self.rotOranges(i, j-1, itr+1)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.answer = []

        for i in range(self.m):
            temp = []
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    temp.append(self.m*self.n)
                else:
                    temp.append(0)
            self.answer.append(temp)
        
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 2:
                    self.rotOranges(i, j, 0)
        result = max([max(self.answer[i]) for i in range(self.m)])
        if result == self.m * self.n:
            return -1

        return result