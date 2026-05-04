class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesMapper = {')' : '(' , '}' : '{' , ']' : '['}

        for bracket in s:
            if bracket not in parenthesesMapper:
                stack.append(bracket)
            else:
                if len(stack) > 0 and stack[-1] == parenthesesMapper[bracket]:
                    stack.pop()
                else:
                    return False
        
        return False if len(stack) > 0 else True
        
         
                
        
        