class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            y = heapq.heappop(minHeap)
            x = heapq.heappop(minHeap)

            if y != x:
                heapq.heappush(minHeap, y-x)
        
        return -minHeap[0] if minHeap else 0