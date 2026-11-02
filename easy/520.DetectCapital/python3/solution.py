
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        start_with_upper = word[0].isupper()
        contain_upper = False
        contain_lower = False

        for i in range(1, len(word)):
            
            letter_is_upper = word[i].isupper()
            if start_with_upper:
                if letter_is_upper:
                    if contain_lower:
                        return False
                    
                    contain_upper=True

                else:
                    if contain_upper:
                        return False
                    
                    contain_lower=True           
            
            elif letter_is_upper:
                return False

        return True
