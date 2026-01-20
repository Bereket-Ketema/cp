class Solution:
    def addDigits(self, num: int) -> int:
        l = list(map(int,str(num)))
        while len(l)>1:
            l = list(map(int,str(sum(l))))
        return l[0]