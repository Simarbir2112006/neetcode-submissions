class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        if people[0] == limit:
            return len(people)

        res = 0
        l, r = 0, (len(people) - 1)

        while l < r:
            while people[r] == limit:
                res += 1
                r   -= 1
            
            total = people[l] + people[r]

            if total > limit:
                r   -= 1
                res += 1
            
            else:
                l   += 1
                r   -= 1
                res += 1

        res += 1 if l==r else 0
        return res