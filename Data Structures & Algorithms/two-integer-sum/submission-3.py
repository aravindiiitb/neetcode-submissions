class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            if nums[i] not in numMap:
                numMap[nums[i]] = i
                if target - nums[i] in numMap:
                    printY = numMap[target - nums[i]]
                    if printY != i:
                        if i < printY:
                            return [i, printY]
                        else:
                            return [printY, i]

        for j in range(len(nums)):
            if target - nums[j] in numMap:
                printY = numMap[target - nums[j]]
                if printY != j:
                    if j < printY:
                        return [j, printY]
                    else:
                        return [printY, j]