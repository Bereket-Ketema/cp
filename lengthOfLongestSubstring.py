class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=list(s[0])
        for k in range(1,len(s)):
            if s[k] not in window:
                window.append(s[k])

        return len(window)

check=Solution()
print (check.lengthOfLongestSubstring("bbbbb"))