class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        tempStack = []
        minVal = self.stack[-1]

        while len(self.stack) > 0:
            minVal = min(minVal, self.stack[-1])
            tempStack.append(self.stack[-1])
            self.stack.pop()
        
        while len(tempStack) != 0:
            self.stack.append(tempStack[-1])
            tempStack.pop()
        
        return minVal


