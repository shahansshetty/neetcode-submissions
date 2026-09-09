from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap=[]
        for x,y in points:
            val=(x**2+y**2)**.5
            heappush(heap,(val,x,y))

        ans=[]
        for _ in range(k):
            temp=[]
            _,x,y=heappop(heap)
            temp.append(x)
            temp.append(y)
            ans.append(temp)

        return ans