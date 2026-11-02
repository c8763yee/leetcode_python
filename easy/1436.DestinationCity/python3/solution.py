class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from_ = set()
        for src, dst in paths:
            from_.add(src)
        
        for _, dst in paths:
            if dst not in from_:
                return dst

        return ''

        