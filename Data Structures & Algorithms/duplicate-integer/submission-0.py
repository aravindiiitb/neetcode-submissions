class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setMap = set(nums)
        return len(setMap) != len(nums)
        