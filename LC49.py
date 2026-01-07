class Solution:
    def tuple_repr(self, string: str) -> tuple:
        a = ord("a")
        r = [0]*26

        for i in string:
            r[ord(i) - a] += 1

        return tuple(r)

    def groupAnagrams(self, strs):
        d = {}
        for i in strs:
            a = self.tuple_repr(i)
            if a in d:
                d[a].append(i)
            else:
                d[a]=[i]
        return list(d.values())