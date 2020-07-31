from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        l = len(s)

        stack = deque()

        if l == 0:
            return True

        if l % 2 != 0:
            return False

        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False

        for i in range(l):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])

            elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                if len(stack):
                    if stack[-1] == '(' and s[i] == ')':
                        stack.pop()
                    elif stack[-1] == '{' and s[i] == '}':
                        stack.pop()
                    elif stack[-1] == '[' and s[i] == ']':
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(stack):
            return False
        else:
            return True
