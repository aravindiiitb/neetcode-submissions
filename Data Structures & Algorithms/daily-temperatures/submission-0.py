class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] #(temp, index)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                topTemp, topIndex = stack.pop()
                output[topIndex] = i - topIndex
            stack.append((temperatures[i], i))
        
        return output
        