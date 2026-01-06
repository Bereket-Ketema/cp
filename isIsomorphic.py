class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check={}
        hello={}
        for i in range(len(s)):
            if t[i] in hello:
                if s[i]==check[t[i]]:
                    continue
                else:
                    return False
            else:
                hello[t[i]]=s[i]
            if s[i] in check:
                if t[i]==check[s[i]]:
                    continue
                else:
                    return False
            else:
                check[s[i]]=t[i]
        return True