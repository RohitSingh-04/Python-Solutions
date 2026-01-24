class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):

            while len(stk) and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()

            if len(stk):
                result[i] = stk[-1] - i
            
            stk.append(i)
        
        return result