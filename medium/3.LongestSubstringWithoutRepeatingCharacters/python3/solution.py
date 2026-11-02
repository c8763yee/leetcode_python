class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}  
        start_index = 0 
        max_length = 0  

        for current_index, character in enumerate(s):
            if character in last_seen and last_seen[character] >= start_index:
                start_index = last_seen[character] + 1
            
            last_seen[character] = current_index
            current_length = current_index - start_index + 1
            max_length = max(max_length, current_length)

        return max_length
