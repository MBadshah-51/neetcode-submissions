class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            else:
                if stack and c == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0