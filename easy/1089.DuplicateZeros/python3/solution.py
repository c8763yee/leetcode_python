class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if arr==[] or 0 not in arr:
            return 
        
        length = len(arr) - 1
        offset = 0
        
        for left_index in range(length+1):
            if left_index >length-offset:
                break
            
            if arr[left_index] == 0:
                if left_index == length - offset: # left_index reach new end
                    arr[length] = 0
                    length -=1
                    break
                
                offset += 1
            
        right = length - offset
        for i in range(right, -1, -1):
            if arr[i]:
                arr[i+offset]  = arr[i]
            else:
                arr[i+offset] = 0
                offset -= 1
                arr[i+offset] = 0

                
                