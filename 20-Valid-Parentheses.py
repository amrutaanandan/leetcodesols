class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['0']
        for i in range(len(s)):
            
            if s[i] == ')' and stack[-1] == '(' and len(stack) > 1:
                stack.pop()
            elif s[i] == '}' and stack[-1] == '{' and len(stack) > 1:
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[' and len(stack) > 1:
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack) != 1:
            return False
        else:
            return True
