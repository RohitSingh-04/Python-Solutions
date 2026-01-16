class Solution:
    def shipable(self, weights, mid, days):
        cap = 0
        for i in weights:
            if cap + i > mid:
                cap = i
                days -= 1
            else:
                cap += i
        return days >= 1

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        s = max(weights)
        e = total

        while s<e:
            mid = (s+e)//2

            if self.shipable(weights, mid, days):
                e = mid
            
            else:
                s = mid + 1
        return s