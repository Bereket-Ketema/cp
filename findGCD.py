class Solution:
    def findGCD(self, nums: list[int]) -> int:
        store = 1
        for i in range(1,max(nums)+1):
            if min(nums)%i == 0 and max(nums)%i ==0:
                store = i
        return store