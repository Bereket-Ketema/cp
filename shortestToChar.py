class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        store = []
        m = s.index(c)
        for i in range(len(s)):
            if s[i] == c:
                m = i
                store.append(0)
            if s[i] != c:
                r = s[i:].find(c)
                if r!=-1:
                    r+=len(s[:i])
                    store.append(min(abs(i-m),abs(i-r)))
                else:
                    store.append(abs(i-m))
        return store     