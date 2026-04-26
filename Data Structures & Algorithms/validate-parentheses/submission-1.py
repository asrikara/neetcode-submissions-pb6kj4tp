class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        plan = { ")" : "(", "]" : "[", "}" : "{" }
        
        for c in s:
            if c in plan:
                if stack and stack[-1] == plan[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True