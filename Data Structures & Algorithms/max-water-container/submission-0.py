class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        low = 0
        high = n -1
        max_volume = 0

        while low < high:
            max_volume = max(max_volume, min(heights[high],heights[low]) * (high - low))

            if heights[low]<= heights[high]:
                low += 1
            else:
                high -= 1
        
        return max_volume