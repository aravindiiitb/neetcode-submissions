class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalMaxMul = 1
        zeroFound = False
        for num in nums:
            if num != 0:
                totalMaxMul = totalMaxMul * num
            else:
                if zeroFound:
                    totalMaxMul = 0
                zeroFound = True               
        
        output = []
        for num in nums:
            if num == 0:
                output.append(totalMaxMul)
            else:
                if zeroFound:
                    output.append(0)
                else:       
                    output.append(int(totalMaxMul/num))

        return output