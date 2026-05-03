class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Freqs = [0] * 26
        s2Freqs = [0] * 26

        for i in range (len(s1)):
            s1Freqs[ord(s1[i]) - ord('a')] += 1
            s2Freqs[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1Freqs[i] == s2Freqs[i]:
                matches += 1
        
        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            charIndex = ord(s2[i]) - ord('a')
            s2Freqs[charIndex] += 1

            if s2Freqs[charIndex] == s1Freqs[charIndex]:
                matches += 1
            elif s2Freqs[charIndex] == s1Freqs[charIndex] + 1:
                matches -= 1
            
            
            charIndexAtLeft = ord(s2[l]) - ord('a')
            s2Freqs[charIndexAtLeft] -= 1
            if s2Freqs[charIndexAtLeft] == s1Freqs[charIndexAtLeft]:
                matches += 1
            elif s2Freqs[charIndexAtLeft] == s1Freqs[charIndexAtLeft] - 1:
                matches -= 1
            
            l += 1
        
        return matches == 26


