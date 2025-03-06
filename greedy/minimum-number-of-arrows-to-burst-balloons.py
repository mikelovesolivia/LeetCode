class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1], x[0]))
        right = points[0][1]
        count = 1
        for i, point in enumerate(points, start=1):
            if point[0] > right:
                right = point[1]
                count += 1
        return count
            
