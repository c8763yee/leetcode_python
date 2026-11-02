def is_vowel(c):
    return chr(ord(c) | 32) in "aeiou"


class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = [(i, e) for i, e in enumerate(s) if is_vowel(e)]
        vowel_index = sorted([i for i, _ in vowel])
        vowel.sort(key=lambda t: (ord(t[1]), t[0]))
        
        ls = list(s)
        for i, idx in enumerate(vowel_index):
            ls[idx] = vowel[i][1]

        return ''.join(ls)

