class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums) + 1)]

        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        for key, v in freq.items():
            count[v].append(key)

        res = []

        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) >= k:
                    return res