class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        l=0
        while l<len(words):
            if words[l]==words[l][::-1]:
                return words[l]
            if l==len(words)-1:
                return ""
            l+=1 
check=Solution()
print(check.firstPalindrome(["abc","car","ada","racecar","cool"]))
            