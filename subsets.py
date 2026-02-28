class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subset=[]
        curr=[]
        def backtrack(start):
            subset.append(curr[:])
            for i in range(start,len(nums)):
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()#when no numbers are left it pops the elements
        backtrack(0)#initializing and adding the empty subset
        return subset
