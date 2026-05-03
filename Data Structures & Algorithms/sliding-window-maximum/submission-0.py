import queue 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indicesQueue = deque()

        l = 0 
        r = 0

        output = []

        while r < len(nums):
            while indicesQueue and nums[indicesQueue[-1]] < nums[r]:
                indicesQueue.pop()
            
            indicesQueue.append(r)

            if indicesQueue[0] < r - k + 1:
                indicesQueue.popleft()
            
            if (r + 1) >= k:
                output.append(nums[indicesQueue[0]])
                l += 1

            r += 1
        
        return output
