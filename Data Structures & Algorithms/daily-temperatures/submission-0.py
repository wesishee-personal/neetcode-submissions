class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        results = [0] * len(temperatures)
        backtrack_stack = []
        
        while i < len(temperatures) - 1:
            j = i + 1

            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    results[i] = j - i
                    break
                j += 1
            i += 1
        
                    
                    
        return results