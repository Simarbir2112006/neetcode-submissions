class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for i in asteroids:
            while s and i < 0 and s[-1] > 0:
                diff = i + s[-1]
                if diff < 0:
                    s.pop()
                elif diff > 0:
                    i = 0
                else:
                    i = 0
                    s.pop()
            if i:
                s.append(i)
        
        return s