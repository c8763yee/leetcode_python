class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested_device = 0
        n = len(batteryPercentages)
        for i in range(n):
            if batteryPercentages[i] == 0:
                continue
            tested_device += 1
            for j in range(i+1, n):
                if batteryPercentages[j] == 0:
                    continue
                    
                batteryPercentages[j] -= 1
        
        return tested_device
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        