class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        h_set = {0:-1}
        s = 0
        for index, i in enumerate(nums):
            s+=i
            if s%k in h_set:
                if (index - h_set[s%k]) >=2:
                    return True
            else:
                h_set[s%k] = index

        return False