class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            #left sorted portion
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle -1 
                else:
                    right = middle + 1
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle -1
                else:
                    right = middle + 1
                    
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1