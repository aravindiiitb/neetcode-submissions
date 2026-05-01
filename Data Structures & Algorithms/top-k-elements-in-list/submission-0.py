class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if num in freqMap:
                freqAndNum = freqMap[num]
                updatedFreq = freqAndNum[0] + 1
                freqMap[num] = (updatedFreq, num)
            else:
                freqMap[num] = (1, num)
        
        freqList = list(freqMap.values())
        freqList.sort(reverse=True)
        output = []
        for k in range(k):
            output.append(freqList[k][1])

        return output    

            

