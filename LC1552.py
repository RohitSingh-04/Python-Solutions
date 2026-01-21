class Solution:
    def possible(self, position, m, mid):
        placed = 1
        prev = position[0]
        for i in position:
            if i - prev >= mid:
                placed += 1
                prev = i
        return placed >= m

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1
        r = position[-1] - position[0]

        while l<r:
            mid = (l+r+1)//2
            if self.possible(position, m, mid):
                l = mid
            else:
                r = mid - 1
        
        return l