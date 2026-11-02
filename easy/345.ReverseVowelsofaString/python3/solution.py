class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'i', 'E', 'U', 'O', 'o', 'a', 'e', 'I', 'u', 'A'} 
        left = 0
        right = len(s)-1
        s = list(s)
        while left < right:
            # switch
            lf = s[left] not in vowels
            rf = s[right] not in vowels
            if not (lf or rf):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -=1
                
            elif lf:
                left += 1
            else:
                right -=1
        return ''.join(s)
