class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ptr1 = 0
        vowel_count = 0
        VOWEL = {'a', 'e', 'i', 'o', 'u'}
        for ptr2 in range(k):
            vowel_count += s[ptr2] in VOWEL
        
        max_cnt = vowel_count
        for ptr2, ele in enumerate(s[k:], k):
            if ele in VOWEL:
                vowel_count += 1
            if s[ptr1] in VOWEL:
                vowel_count -= 1
            max_cnt = max(max_cnt, vowel_count)
            ptr1 += 1
            

        return max_cnt