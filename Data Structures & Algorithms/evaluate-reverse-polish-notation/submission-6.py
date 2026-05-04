def plusOperator(a, b):
        return a + b

def multiplyOperator(a, b):
    return a * b

def divideOperator(a , b):
    return int(a/b)

def subtractOperator(a, b):
    return a - b    
    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+': 1, '*': 1, '-': 1, '/': 1}

        for c in tokens:
            intermVal = 0
            if c == '+':
                intermVal = plusOperator(stack.pop(), stack.pop())
            elif c == '-':
                a = stack.pop()
                b = stack.pop()
                intermVal = subtractOperator(b, a)
            elif c == '*':
                intermVal = multiplyOperator(stack.pop(), stack.pop())
            elif c == '/':
                a = stack.pop()
                b = stack.pop()
                intermVal = divideOperator(b, a)
            else:
                stack.append(int(c))
            
            if c in operators:
                stack.append(intermVal)
        
        return stack[0]



        