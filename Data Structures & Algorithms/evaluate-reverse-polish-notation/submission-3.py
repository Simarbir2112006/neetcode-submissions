class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for i in tokens:
            if i == '+':
                total = s.pop() + s.pop()
                s.append(total)
            elif i == '-':
                n1 = s.pop()
                n2 = s.pop()
                sub = n2 - n1
                s.append(sub)
            elif i == '*':
                mul = s.pop() * s.pop()
                s.append(mul)
            elif i == '/':
                n1 = s.pop()
                n2 = s.pop()
                div = int(n2/n1)
                s.append(div)
            else:
                s.append(int(i))
        
        return s[-1]