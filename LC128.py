class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)

        result = 0

        for i in d:
            if i - 1 in d:
                continue
                
            current = 1
            temp = i
            while temp+1 in d:
                current += 1
                temp += 1

            result = max(result, current)

        return result