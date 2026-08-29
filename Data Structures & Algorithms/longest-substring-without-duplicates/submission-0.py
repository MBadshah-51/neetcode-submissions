class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        count = defaultdict(int)
        max_len = 0

        l = r = 0
        
        while r < n:
            count[s[r]] += 1

            while l < r and count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
