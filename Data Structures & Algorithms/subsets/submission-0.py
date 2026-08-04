class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, current = [], []
        n = len(nums)
        i = 0

        def backtrack(i: int):
            if i == n:
                #index out of bounds
                result.append(current[:])
                return
            #don't pick nums[i]
            backtrack(i+1)

            #do pick nums[i]
            current.append(nums[i])
            backtrack(i+1)
            current.pop()

        backtrack(0)
        return result        
                

