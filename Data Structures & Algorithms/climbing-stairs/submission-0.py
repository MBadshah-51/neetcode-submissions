class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        n1 = 1
        n2 = 2
        res = 0
        for i in range(3, n+1):
            res = n1 + n2
            n1 = n2
            n2 = res

        return res