class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        dt = defaultdict(int)

        for ch in s:
            dt[ch] += 1
        
        for ch in t:
            if ch in dt and dt[ch]> 0:
                dt[ch] -=1 
            else:
                return False
        
        for value in dt.values():
            if value != 0:
                return False
        
        return True