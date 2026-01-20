class Solution:
    def gcd(self,n,m):
        store = 1
        for i in range(1,max(n,m)+1):
            if n % i == 0 and m % i == 0:
                store = i
        return store
    def countBeautifulPairs(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if self.gcd(int(str(nums[i])[0]),nums[j] % 10) == 1:
                    count+=1
        return count

check = Solution()
print(check.countBeautifulPairs( [31,25,72,79,74]))