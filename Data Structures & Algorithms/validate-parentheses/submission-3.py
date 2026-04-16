class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if (char == '(') or (char == '[') or (char == '{'):
                stack.append(char)
            else:
                temp = stack.pop() if stack else 0
                if char == ')':
                    if temp != '(':
                        return False
                if char == ']':
                    if temp != '[':
                        return False
                if char == '}':
                    if temp != '{':
                        return False
        
        return False if stack else True