class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
            
        freqNums = [[] for i in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            freqNums[freq].append(num)
        
        output = []

        for items in freqNums[::-1]:
            for num in items:
                if k == 0:
                    return output
                else: 
                    output.append(num)
                    k -= 1

        return output    

            

