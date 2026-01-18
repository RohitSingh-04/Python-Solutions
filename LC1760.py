from math import ceil
class Solution:
    def possible(self, nums, maxOperations, mid):
        opr = 0
        for i in nums:
            opr += ceil(i / mid) - 1

            if opr > maxOperations:
                return False
        
        return True

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        s = 1
        l = max(nums)

        while s<l:
            mid = (s + l) // 2
            if self.possible(nums, maxOperations, mid):
                l = mid
            else:
                s = mid + 1
        
        return s