class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        is_valid = True

        # Dictionary to match closing with opening
        matching = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '({[':
                stack.append(c)  # push opening brackets
            elif c in ')}]':
                if stack and stack[-1] == matching[c]:
                    stack.pop()  # matched, pop it
                else:
                    is_valid = False  # either stack empty or not matching
                    break
        return(is_valid and len(stack) == 0)