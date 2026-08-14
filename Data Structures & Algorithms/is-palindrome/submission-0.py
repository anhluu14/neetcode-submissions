class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        L = 0
        R = n - 1

        while L < R:
            #if the character at L is not alpha numeric we just want to move on
            if not s[L].isalnum():
                L += 1
                continue
            
            if not s[R].isalnum():
                R -= 1
                continue
            
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
        
        return True