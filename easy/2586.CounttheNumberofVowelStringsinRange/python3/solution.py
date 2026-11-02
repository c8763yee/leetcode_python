class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return len([i for i in words[left:right+1] if all(i[idx] in 'aeiou' for idx in (0,-1))])