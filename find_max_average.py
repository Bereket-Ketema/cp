class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        window=sum(nums[:k])
        maxs=window

        for i in range(len(nums)-k):
            window=window-nums[i]+nums[i+k]
            maxs = max(window,maxs)
        
        average=float(maxs)/k
        return average

check=Solution()
print (check.findMaxAverage([1,12,-5,-6,50,3],4))