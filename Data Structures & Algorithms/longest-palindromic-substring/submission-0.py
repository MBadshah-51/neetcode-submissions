class Solution:
    def traverse(self, s: str, ans: list, i, j):
        n = len(s)
        while 0 <= i and j < n \
                and s[i] == s[j]:
                
                if (j - i + 1) > ans[0]:
                    ans[0] = j - i + 1
                    ans[1] = s[i: j+1]

                i -= 1
                j += 1
        
    def longestPalindrome(self, s: str) -> str:
        
        ans = [0, ""]

        n = len(s)

        for start in range(n):
            #odd length
            i = j = start
            self.traverse(s, ans, i, j)
            
            #even length
            i = start
            j = start + 1
            self.traverse(s, ans, i , j)
        
        return ans[1]