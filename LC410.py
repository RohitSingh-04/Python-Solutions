class Solution:
    def possible(self, nums, k, mid):

        s = 0
        for i in nums:
            s += i
            if s > mid:
                s = i
                k-=1

            if k == 0:
                return False

        return True

    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        h = sum(nums)

        while l<h:
            mid = (l+h)//2
            if self.possible(nums, k, mid):
                h = mid
            else:
                l = mid + 1
        
        return l