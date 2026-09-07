class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [0] * len(points)

        for i, point in enumerate(points):
            x, y = point
            distance[i] = (math.sqrt(x**2 + y**2), [x, y])
        
        # distance = [(-dis, pt) for dis, pt in distance]
        heapq.heapify(distance)

        res = []
        while len(res) < k:
            res.append(heapq.heappop(distance)[1])
        
        return res

        