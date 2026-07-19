class TimeMap:

    def __init__(self):
        self.data = {} #{key, [(value, timestamp)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.data or timestamp < self.data[key][0][1]:
            return "" 
        
        l = 0
        r = len(self.data[key]) - 1
        res = self.data[key][0]
        print(key, timestamp, self.data)

        while l <= r:
            m = (l + r) // 2
            curr = self.data[key][m][1]

            if curr == timestamp: 
                res = self.data[key][m]
                break
            elif curr <= timestamp:
                if curr > res[1]:
                    res = (self.data[key][m][0], curr)
                l = m + 1
            else:
                r = m - 1
            
        return res[0]

        
