class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        freqMapT = {}
        for c in t:
            freqMapT[c] = 1 + freqMapT.get(c, 0)
        
        currFreqMap = {}

        have = 0
        need = len(freqMapT)
        l = 0
        
        resIndices = [-1, -1]
        minLen = float("infinity")

        for r in range(len(s)):
            currFreqMap[s[r]] = 1 + currFreqMap.get(s[r], 0)

            if s[r] in freqMapT and currFreqMap[s[r]] == freqMapT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    resIndices = [l,r]

                currFreqMap[s[l]] -= 1
                if s[l] in freqMapT and currFreqMap[s[l]] < freqMapT[s[l]]:
                    have -= 1

                l += 1
        
        l, r = resIndices
        return s[l: r + 1] if minLen != float("infinity") else ""

