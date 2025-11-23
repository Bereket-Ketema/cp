class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=list(bin(int(a,2)+int(b,2)))
        result.pop(0)
        result.pop(0)
        checks=''.join(result)
        return checks