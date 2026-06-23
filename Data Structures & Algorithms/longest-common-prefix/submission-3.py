class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for i in range(len(strs[0])):
            for j in range(0, len(strs)):
                if len(strs[j]) > i  and strs[j][i] == strs[0][i]:
                    continue
                else:
                    return lcp
            
            lcp += strs[0][i]
        
        return lcp