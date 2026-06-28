class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        freq_sorted = sorted(freq.items(), key = lambda item: item[1], reverse=True)
        
        res = []

        for i in range(k):
            res.append(freq_sorted[i][0])

        return res