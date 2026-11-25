class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = n
        count = 0
        while temp:
            if temp & 1 == 1:
                count += 1
            temp = temp >>1
        
        return count
        