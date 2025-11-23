class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r,store=len(s)-1,0
        while r>=0 and s[r].isspace():
            r-=1
        while r>=0 and not s[r].isspace():
            store+=1
            r-=1
        return store