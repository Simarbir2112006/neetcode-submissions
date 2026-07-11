class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)
        s.append([temperatures[0], 0])

        for i in range(len(temperatures)):
            val = temperatures[i]
            while s and s[-1][0] < val:
                idx = s[-1][1]
                res[idx] = i - idx
                s.pop()
            s.append([val, i])
        
        return res