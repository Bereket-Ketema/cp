class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result=[]
        result.append(nums[0])
        l=1
        while l<len(nums):
            result.append(nums[l]+result[-1])
            l+=1
        return result