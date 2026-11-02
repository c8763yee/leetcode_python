def manacher(s):
    # Step 1: Pad the string with '#' to handle even-length palindromes uniformly
    padded_s = '#' + '#'.join(s) + '#'
    n = len(padded_s)
    
    # Array to store the maximum radius of palindromes centered at each position
    palindrome_radii = [0] * n
    
    # The center and right edge of the current right-most palindrome
    center = 0
    right_edge = 0

    for i in range(n):
        # Calculate the initial radius of the palindrome centered at i
        if i < right_edge:
            mirror_i = 2 * center - i
            palindrome_radii[i] = min(right_edge - i, palindrome_radii[mirror_i])
        else:
            palindrome_radii[i] = 1

        # Expand the palindrome centered at i
        while (i + palindrome_radii[i] < n and i - palindrome_radii[i] >= 0 and 
               padded_s[i + palindrome_radii[i]] == padded_s[i - palindrome_radii[i]]):
            palindrome_radii[i] += 1
        
        # Update the center and right edge if the expanded palindrome is beyond the current right edge
        if i + palindrome_radii[i] - 1 > right_edge:
            center = i
            right_edge = i + palindrome_radii[i] - 1

    return palindrome_radii

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Step 1: Get the palindrome radii using the Manacher's algorithm
        palindrome_radii = manacher(s)
        print(palindrome_radii)
        # Step 2: Find the longest palindrome length and its center position in the padded string
        max_length = 0
        center_index = 0
        for i, radius in enumerate(palindrome_radii):
            if radius > max_length:
                max_length = radius
                center_index = i

        # Step 3: Convert the center index and radius back to the original string context
        start = (center_index - max_length + 1) // 2
        end = (center_index + max_length - 1) // 2

        # Step 4: Extract the longest palindromic substring from the original string
        longest_palindrome = s[start:end]

        return longest_palindrome
