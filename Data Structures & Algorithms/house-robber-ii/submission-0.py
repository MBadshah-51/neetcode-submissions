class Solution:
    def solve(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]
        
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        
        return dp[n]

    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        return max(self.solve(nums[1:]), self.solve(nums[:-1]))