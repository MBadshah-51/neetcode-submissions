class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        n = len(nums)
        max_len = 0
        
        for num in set_num:
            if num-1 in set_num:
                continue
            
            length = 1
            while num + length in set_num:
                length += 1

            max_len = max(max_len, length)
        
        return max_len
            