class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False   

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()

        for w in words:
            curr = root
            for ch in w:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.end = True
            
        
        
        ans = []
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] not in node.children or (r, c) in visited):
                return False
            
            ch = board[r][c]
            nxt = node.children[ch]
            word += ch

            if nxt.end:
                ans.append(word)
                nxt.end = False

            visited.add((r,c))
            res = (
                dfs(r + 1, c, nxt, word) or
                dfs(r - 1, c, nxt, word) or
                dfs(r, c + 1, nxt, word) or
                dfs(r, c - 1, nxt, word))
            
            visited.remove((r,c))
            
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return ans