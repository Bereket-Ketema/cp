class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result=[]
        for num in nums:
            result.append(pow(num,2))
        result.sort()
        return result
check=Solution()
print(check.sortedSquares([-4,-1,0,3,10]))