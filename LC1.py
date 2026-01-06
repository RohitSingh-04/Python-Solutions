class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t_sum = {}
        for index, i in enumerate(nums):
            if target - i in t_sum:
                return [t_sum[target-i], index]
            t_sum[i] = index