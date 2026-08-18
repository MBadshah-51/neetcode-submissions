class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        from collections import defaultdict
        dt1 = defaultdict(int)
        dt2 = defaultdict(int)

        for i in range(len(s)):
            dt1[s[i]] += 1
            dt2[t[i]] += 1

        return dt1 == dt2