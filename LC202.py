from functools import lru_cache
class Solution:
    @staticmethod
    @lru_cache(maxsize = 128)
    def squarer(x):
        if x<10:
            return x*x
        result = 0
        while x > 0:
            result += (x%10)**2
            x//=10
        return result

    def isHappy(self, n: int) -> bool:
        s = n
        f = n
        while f > 1: 
            print(s,f)
            s = self.squarer(s)
            f = self.squarer(f)
            print(f)
            f = self.squarer(f)
            print(s, f)
            if s == f and f != 1:
                return False
        
        return f == 1