def plusOperator(a, b):
        return a + b

def multiplyOperator(a, b):
    return a * b

def divideOperator(a , b):
    return math.floor(a/b)

def subtractOperator(a, b):
    return a - b    
    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+': 1, '*': 1, '-': 1, '/': 1}

        i = 0
        while i < len(tokens):
            while tokens[i] not in operators:
                stack.append(int(tokens[i]))
                i += 1
            
            intermVal = 0
            if tokens[i] == '+':
                intermVal = plusOperator(stack.pop(), stack.pop())
            elif tokens[i] == '-':
                a = stack.pop()
                b = stack.pop()
                intermVal = subtractOperator(b, a)
            elif tokens[i] == '*':
                intermVal = multiplyOperator(stack.pop(), stack.pop())
            elif tokens[i] == '/':
                a = stack.pop()
                b = stack.pop()
                intermVal = divideOperator(b, a)
            
            
            stack.append(intermVal)
            i += 1
        
        return stack[0]



        