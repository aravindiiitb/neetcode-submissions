class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[j].isalnum() == False:
                j -= 1
            
            if s[i].isalnum() == False:
                i += 1

            if s[i].casefold() == s[j].casefold():
                j -= 1
                i += 1
            else:
                if i >= j:
                    return True
                return False
        return True