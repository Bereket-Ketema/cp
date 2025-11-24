class Solution:
    def maxScore(self, s: str) -> int:
        score,r=0,0
        left=''
        for i in range(1,len(s)):
            left+=s[r]
            zero=left.count('0')
            one=s[i:].count('1')
            score=max(score,zero+one)
            r+=1
        return score
