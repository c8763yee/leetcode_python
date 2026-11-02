class Solution:
    def simplifyPath(self, path: str) -> str:
        slashed = False
        lst = []
        for p in path.split('/'):
            if p == "" or (lst == [] and (p == '..' or p == '.')):
                continue

            if lst and p == '..':
                lst.pop()
            elif p != '.':
                lst.append(p)
        
        return '/' + '/'.join(lst)