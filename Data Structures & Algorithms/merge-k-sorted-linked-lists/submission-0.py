# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        head = ListNode(-1)
        temp = head

        import heapq
        heap = []

        for i in range(n):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        
        while heap:
            val, index = heapq.heappop(heap)
            
            temp.next = lists[index]
            lists[index] = lists[index].next
            temp = temp.next

            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
        
        return head.next