class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allMap = {}
        for num in nums:
            allMap[num] = 1
        
        longest = 0
        for num in nums:
            curr_long = 0
            while num in allMap:
                curr_long += 1
                num += 1
            if longest < curr_long:
                longest = curr_long
        
        return longest

                
        
        