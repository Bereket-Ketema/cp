class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        size=nums.count(val)
        for i in range(size):
            nums.remove(val)
        return len(nums)