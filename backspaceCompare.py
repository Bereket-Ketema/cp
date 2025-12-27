class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(text):
            result = ""
            for ch in text:
                if ch == '#':
                    result = result[:-1]
                else:
                    result += ch
            return result

        return process(s) == process(t)
