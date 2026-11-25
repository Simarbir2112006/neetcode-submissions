class Solution:
    def countSubstrings(self, s: str) -> int:
        # done = set()
        res = 0
        n = len(s)

        for i in range(n):
            l = i
            r = i

            while l >= 0 and r < n and s[l] == s[r]:
                # curr = s[l:r+1]
                # if curr not in done:
                #     done.add(curr)
                res += 1
                l -= 1
                r += 1

            l = i
            r = i + 1

            while l >= 0 and r < n and s[l] == s[r]:
                # curr = s[l:r+1]
                # if curr not in done:
                #     done.add(curr)
                res += 1
                l -= 1
                r += 1
        
        return res