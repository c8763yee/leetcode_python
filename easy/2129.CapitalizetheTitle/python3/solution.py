class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(map(lambda x: x[0].upper() + x[1:].lower() if len(x)>2 else x.lower(), 
        title.split()))