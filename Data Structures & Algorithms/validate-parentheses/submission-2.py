class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if (c == '(') or (c == '[') or (c == '{'):
                stack.append(c)
            else:
                if len(stack) == 0 : 
                    return False

                top = stack[-1]
                stack.pop()
                if (c == ')' and top != '(') or (c == ']' and top != '[') or (c == '}' and top != '{'):
                    return False
        return not stack
