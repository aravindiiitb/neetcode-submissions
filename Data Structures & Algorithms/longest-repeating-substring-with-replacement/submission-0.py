class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0        

        freqMap = {}
        mostFreqCharCount = 0
        res = 0

        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)

            mostFreqCharCount = max(mostFreqCharCount, freqMap[s[r]])

            while r - l + 1 - mostFreqCharCount > k:
                freqMap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res





        