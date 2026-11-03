class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n-1] = 0 if s[-1] == "0" else 1

        for i in range(n -2, -1, -1):
            if s[i] == "0": continue
            if s[i] == "1":
                dp[i] = dp[i+1] + dp[i+2]
            elif s[i] == "2" and\
             0 <= ord(s[i+1]) - ord("0") < 7:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        
        return dp[0]