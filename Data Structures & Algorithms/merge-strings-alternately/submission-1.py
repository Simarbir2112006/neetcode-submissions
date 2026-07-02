class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        w2 = 0

        merged_word = []

        while w1 < len(word1) and w2 < len(word2):
            merged_word.append(word1[w1])
            merged_word.append(word2[w2])
            w1+=1
            w2+=1
        
        if w1 < len(word1):
            merged_word.append(word1[w1:])

        if w2 < len(word2):
            merged_word.append(word2[w2:])
        
        return "".join(merged_word)