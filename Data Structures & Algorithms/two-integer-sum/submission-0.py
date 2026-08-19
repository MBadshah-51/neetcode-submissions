class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        dt = {}

        for i in range(n):
            key = target - nums[i]
            if key in dt:
                return [dt[key], i]
            dt[nums[i]] = i
        
        return [-1,-1]