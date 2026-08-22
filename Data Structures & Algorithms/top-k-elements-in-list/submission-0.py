class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        import heapq

        for key, value in count.items():
            heapq.heappush(heap,(value,key))
            
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for _, key in heap:
            ans.append(key)
        
        return ans