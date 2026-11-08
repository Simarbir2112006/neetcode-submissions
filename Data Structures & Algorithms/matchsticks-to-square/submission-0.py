class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        side = total // 4

        matchsticks.sort(reverse=True)

        def backtrack(i, sq):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sq[j] + matchsticks[i] <= side:
                    sq[j] += matchsticks[i]
                    if backtrack(i+1, sq):
                        return True
                    sq[j] -= matchsticks[i]
            
            return False

        return backtrack(0, [0, 0, 0, 0])