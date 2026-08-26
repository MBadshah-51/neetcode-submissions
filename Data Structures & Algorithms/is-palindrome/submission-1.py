class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        low = 0
        high = n-1

        while low < high:

            while low < n and not s[low].isalnum():
                low += 1
            while high > 0 and not s[high].isalnum():
                high -=1
            
            if low >= high:
                break
            
            if s[low].lower() == s[high].lower():
                low += 1
                high -=1
            else:
                return False
        
        return True