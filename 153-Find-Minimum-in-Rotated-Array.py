class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        
 #l = left, r = right, mid = middle index
 
        if length == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
        
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
        
            if nums[r] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
