class Solution:
    def rowWithMax1s(self, arr):
        maximum=0
        index=0
        for row in range(len(arr)):
            curr=arr[row].count(1)
            if curr>maximum:
                maximum=curr
                index=row
        if maximum==0:
            return -1
        return index
