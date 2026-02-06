class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        buffer = [(point[0]**2 + point[1]**2 , index) for index, point in enumerate(points)]

        buffer.sort(key=lambda x: x[0])
        
        answer = [points[buffer[i][1]] for i in range(k)]

        return answer