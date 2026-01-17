class Solution:
    def possible(self, bloomDay, m, k, mid):
        count = 0
        adj = 0
        for i in bloomDay:

            if i <= mid:
                adj += 1
            else:
                adj = 0

            if adj == k:
                count += 1
                adj = 0
        
        return count >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < k*m:
            return -1 

        s = min(bloomDay)
        l = max(bloomDay)

        while s < l:
            mid = (s+l) // 2
            if self.possible(bloomDay, m, k, mid):
                l = mid
            else:
                s = mid + 1
        
        return s