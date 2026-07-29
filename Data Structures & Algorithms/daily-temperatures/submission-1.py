class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        backtrack_stack = []
        
        for i, temp in enumerate(temperatures):
            while backtrack_stack and temp > backtrack_stack[-1][1]:
                stack_index, stack_temp = backtrack_stack.pop()
                results[stack_index] = (i - stack_index)
            backtrack_stack.append([i, temp])
        return results