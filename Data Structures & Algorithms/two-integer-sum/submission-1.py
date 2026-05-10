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