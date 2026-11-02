from typing import List

def condition(mid, arr, m):
    # Placing the first ball in the first basket
    count = 1
    last_position = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] - last_position >= mid:
            # Placing the next ball
            count += 1
            last_position = arr[i]
        if count == m:
            return True
    return False

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        left = 1
        right = position[-1] - position[0]  # The maximum possible distance
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if condition(mid, position, m):
                result = mid
                left = mid + 1  # Try for a larger distance
            else:
                right = mid - 1  # Try for a smaller distance
        
        return result
