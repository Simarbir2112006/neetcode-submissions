class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0

        while l <= r:
            m = (l + r) // 2
            sq_m = m * m

            if sq_m == x:
                return m

            elif sq_m < x:
                l = m + 1
                res = m

            else:
                r = m - 1

        return res