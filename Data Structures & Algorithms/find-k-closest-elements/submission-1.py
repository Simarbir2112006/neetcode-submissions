class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        idx = 0
        bool_mid = False
        res = []

        while l <= r:
            mid = (l+r) // 2

            if arr[mid] == x:
                idx = mid
                bool_mid = True
                break
            
            elif arr[mid] > x:
                r = mid - 1
            
            else:
                l = mid + 1
        
        if not bool_mid:
            idx = min(l, len(arr) - 1)

        l = idx - 1
        r = idx

        for i in range(k):
            a = arr[l] if l > -1 else float('inf')
            b = arr[r] if r < len(arr) else float('inf')

            if (abs(a - x) < abs(b - x)) or ((abs(a - x) == abs(b - x)) and a < b):
                res.append(a)
                l -= 1
            else:
                res.append(b)
                r += 1
        res.sort()
        return res
