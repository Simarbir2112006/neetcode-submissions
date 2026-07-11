class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        n = len(path)
        paths = path.split('/')

        for i in paths:
            if i == '' or i == '.':
                pass
            elif i == '..':
                if res:
                    res.pop()
            else:
                res.append(i)

        return '/' + '/'.join(res)

