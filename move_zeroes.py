class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l,r=0,1
        while r<len(nums):
            if nums[l] ==0 and nums[r]==0:
                r+=1
            elif nums[l]==0 or nums[r]==0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1;r+=1
            else:
                r+=1
        return nums