class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        low = 0
        high = n-1

        while low < high:

            while low < high and not s[low].isalnum():
                low += 1
            while high > low and not s[high].isalnum():
                high -=1
            
            if s[low].lower() != s[high].lower():
                return False
            low += 1
            high -=1
        
        return True