class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""

        for i in strs:
            leng = len(i)
            ret += f'{leng}' + '#' + i

        return ret 

    def decode(self, s: str) -> List[str]:
        ret = []
        if len(s) == 0:
            return ret 

        curr = 0

        while True:
            # Calculate leng of str
            leng=''
            for c in range(curr, len(s)):
                if s[c]!= '#':
                    leng += s[c]
                    curr +=1
                else:
                    curr +=1
                    break

            string = ''
            start = curr
            try:
                leng_int = int(leng)
            except ValueError:
                raise ValueError(f"Indexing was wrong fix it: {leng}") 

            while curr < int(leng) + start:
                string+= s[curr]
                curr+=1
            ret.append(string)

            if curr >= len(s):
                return ret
            