class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        # Initialize result array with 0s
        result = [0] * (n + 1)
        # Track used numbers
        used = [False] * 10
        
        def canPlace(pos: int, num: int, pattern: str) -> bool:
            # If number is already used
            if used[num]:
                return False
                
            # For first position, we can place any number
            if pos == 0:
                return True
                
            # Check if current placement satisfies pattern
            if pattern[pos-1] == 'I':
                return result[pos-1] < num
            else:  # pattern[pos-1] == 'D'
                return result[pos-1] > num
        
        def backtrack(pos: int, pattern: str) -> bool:
            # If we've filled all positions, we've found a solution
            if pos == n + 1:
                return True
                
            # Try each number from 1 to 9
            for num in range(1, 10):
                if canPlace(pos, num, pattern):
                    result[pos] = num
                    used[num] = True
                    
                    if backtrack(pos + 1, pattern):
                        return True
                        
                    # Backtrack
                    used[num] = False
                    result[pos] = 0
                    
            return False
            
        # Start backtracking from position 0
        backtrack(0, pattern)
        return ''.join(map(str, result))