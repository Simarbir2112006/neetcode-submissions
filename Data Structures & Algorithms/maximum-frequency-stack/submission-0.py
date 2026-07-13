class FreqStack:

    def __init__(self):
        self.s = []
        self.freq = {}

    def push(self, val: int) -> None:
        self.s.append(val)
        self.freq[val] = 1 + self.freq.get(val, 0)
        # print("push")
        # print(self.s)
        # print(self.freq)


    def pop(self) -> int:
        max_val = max(self.freq.values())
        max_keys = set()
        for k, v in self.freq.items():
            if v == max_val:
                max_keys.add(k)

        # print("pop")
        # print(self.s)
        # print(self.freq)
        # print(max_val)
        # print(max_keys)
        for i in range(len(self.s) - 1, -1, -1):
            if self.s[i] in max_keys:
                self.freq[self.s[i]] -= 1
                return self.s.pop(i)


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()