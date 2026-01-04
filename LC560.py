class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0

        current_sum = 0 
        prefix = {0: 1}
        
        for i in nums:
            current_sum += i

            if current_sum-k in prefix:
                total += prefix[current_sum - k]

            prefix[current_sum] = prefix.get(current_sum, 0)+1


        return total