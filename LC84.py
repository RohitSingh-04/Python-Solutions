class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        left_smaller = [-1]*len(heights)
        right_smaller = [len(heights)]*len(heights)
        stk = []
        
        for i in range(len(heights) - 1, -1, -1):
            while(len(stk) and heights[stk[-1]] >= heights[i]):
                stk.pop()

            if len(stk):
                right_smaller[i] = stk[-1]

            stk.append(i)

        stk.clear()
        for i in range(len(heights)):
            while(len(stk) and heights[stk[-1]] >= heights[i]):
                stk.pop()
            
            if len(stk):
                left_smaller[i] = stk[-1]
            
            stk.append(i)
        
        ans = 0
        for i in range(len(heights)):
            current = heights[i] * (right_smaller[i] - left_smaller[i] - 1)
            print(current)
            ans = max(current, ans)

        return ans
                

