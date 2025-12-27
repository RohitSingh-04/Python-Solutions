
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        max_window = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):

            if s[r] not in freq_map:
                freq_map[s[r]] = 1
            else:
                freq_map[s[r]] += 1
            
            max_freq = max(max_freq, freq_map[s[r]])

            if ((r-l)+1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1
            
            max_window = max(max_window, r-l+1)

        return max_window