import heapq
class Solution:
  def minOperations(self, arr):
    total=sum(arr)
    target=total/2
    
    maxheap=[-x for x in arr]
    heapq.heapify(maxheap)

    curr=total
    count=0
    while curr>target:
        val=-heapq.heappop(maxheap)
        half=val/2
        curr-=half
        count+=1
        heapq.heappush(maxheap,-half)
    
    return count
