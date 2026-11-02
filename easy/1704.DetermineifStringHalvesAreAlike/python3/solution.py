class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # left = s[:l//2]
        # right = s[l//2:]
        l = len(s)
        vowel = 0
        VOWEL = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i, c in enumerate(s, 1):
            if c in VOWEL:
                vowel += 1
            if s[l-i] in VOWEL:
                vowel -= 1
            if l - i <= i:
                break

        return vowel == 0