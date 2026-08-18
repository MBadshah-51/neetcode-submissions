class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        dt = set()

        for num in nums:
            if num in dt:
                return True
            dt.add(num)
        
        return False
