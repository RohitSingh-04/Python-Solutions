class Solution:

    def caneat(self, piles, mid, h):

        total_time = 0
        for i in piles:
            total_time += i//mid
            if i % mid != 0:
                total_time += 1
        
        return total_time <=h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = sum(piles)

        l = 1
        r = max(piles)

        while l<r:
            mid = (l+r)//2

            if self.caneat(piles, mid, h):
                r = mid
            
            else:
                l = mid + 1

        return l