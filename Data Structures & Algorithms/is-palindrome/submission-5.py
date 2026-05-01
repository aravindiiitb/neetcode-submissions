class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[j].isalnum() == False:
                j -= 1
                continue
                
            if s[i].isalnum() == False:
                i += 1
                continue

            if s[i].casefold() == s[j].casefold():
                j -= 1
                i += 1
            else:    
                return False
        return True