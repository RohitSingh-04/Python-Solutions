from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or s == "":
            return ""

        freq_required = Counter(t)
        required = len(t)

        l = 0
        result = ""
        min_len = float("inf")

        for r in range(len(s)):
            if s[r] in freq_required:
                if freq_required[s[r]] > 0:
                    required -= 1
                freq_required[s[r]] -= 1

            while required == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    result = s[l:r+1]

                if s[l] in freq_required:
                    freq_required[s[l]] += 1
                    if freq_required[s[l]] > 0:
                        required += 1
                l += 1

        return result
