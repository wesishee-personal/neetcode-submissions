class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        a = 0
        results = []
        while a < len(nums)-2:
            l = a+1
            r = len(nums)-1
            while l < r:
                if l-1 > a and [l-1] == nums[l]:
                    l += 1
                    continue
                if r < len(nums) -1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                current_sum = nums[a] + nums[l] + nums[r]
                if  current_sum == 0:
                    #found match
                    results.append([nums[a], nums[l], nums[r]])
                if current_sum < 0:
                    l += 1
                    continue
                else:
                    r -= 1
                    continue
            a += 1
            while a <= len(nums)-1 and nums[a-1] == nums[a]:
                a+=1
        return results
            



