from math import ceil
class Solution:
    def condition(self, nums, mid, threshold):
        s = 0
        for i in nums:
            s += ceil(i/mid)
        return s <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        s = 1
        e = max(nums)

        while s<e:
            mid = (s+e)//2
            if self.condition(nums, mid, threshold):
                e = mid
            else:
                s=mid + 1
        
        return s
