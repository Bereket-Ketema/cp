class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = "".join([c.lower() for c in s if c.isalpha() or c.isdigit()])
        return True if z==z[::-1] else False
    
check=Solution()
print(check.isPalindrome("0P"))