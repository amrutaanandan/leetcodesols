#solution 1:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] = 999
                
                k+=1
        nums.sort()

        return len(nums)-k

  #solution 2:
  class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
                i-=1
            i+=1
        return len(nums)
