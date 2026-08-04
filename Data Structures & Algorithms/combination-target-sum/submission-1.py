class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, current = [], []

        def backtrack(i: int, current_sum):

            if current_sum == target:
                result.append(current[:])
                return
            elif current_sum > target or i >= len(nums):
                return
            # don't pick current num
            backtrack(i+1, current_sum)

            # do pick current num
            current.append(nums[i])
            backtrack(i, current_sum+nums[i])
            current.pop()

        backtrack(0,0)
        return result