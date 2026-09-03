class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        count = 0
        dt = Counter(t)

        l = r = 0
        min_len = float('inf')
        ans = ""

        while r < n:
            if dt[s[r]] > 0:
                count += 1
            dt[s[r]] -= 1

            while count == m: 
                if min_len > (r - l + 1):
                    min_len = r - l + 1
                    ans = s[l:r+1]

                if dt[s[l]] >= 0:
                    count -= 1

                dt[s[l]] += 1
                l += 1
            
            r += 1
        
        return ans

            