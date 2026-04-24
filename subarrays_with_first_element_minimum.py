class Solution:
    def countSubarrays(self, arr):
        n=len(arr)
        count=0
        for i in range(n):
            for j in range(i,n):
                if arr[j]<arr[i]:
                    break
                count+=1
        return count
