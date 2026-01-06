class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        l, r = 0,s.index(c)
        store = []

        while l<len(s):
            m = len(s)
            if s[l] == c:
                if l !=r:
                    m = l
                store.append(0)
            if s[l] != c:
                store.append(min(abs(r-l),abs(r-m)))
            l+=1
        return store


check = Solution()
print(check.shortestToChar(s = "loveleetcode", c = "e"))      
