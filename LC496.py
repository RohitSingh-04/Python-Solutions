class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        buffer = {}
        stk = [-1]

        for p in range(len(nums2)-1, -1, -1):
            buffer[nums2[p]] = -1
            while len(stk):
                if nums2[p] < stk[-1]:
                    buffer[nums2[p]] = stk[-1]
                    stk.append(nums2[p])
                    break
                stk.pop()
            stk.append(nums2[p])


        return [buffer[i] for i in nums1]
