class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = []
        for i in range(len(nums)):
            if i == 0:
                prefix_arr.append(1)
            else:
                prefix_arr.append(nums[i-1] * prefix_arr[-1])
        
        suffix_arr = []
        for j in range(len(nums), 0, -1):
            if j == len(nums):
                suffix_arr.insert(0, 1)
            else:
                suffix_arr.insert(0, nums[j]*suffix_arr[0])    

        print(suffix_arr)

        output = []
        for i in range(len(nums)):
            output.append(prefix_arr[i] * suffix_arr[i])
        
        return output
