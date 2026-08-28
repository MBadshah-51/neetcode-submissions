class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        low = 0
        high = n-1

        res = nums[low]

        while low <= high:
            mid = (low + high)//2

            res = min(nums[mid], res)

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1

        return res