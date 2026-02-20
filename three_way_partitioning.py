class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, arr, a, b):
	    # code here 
	    arr1=[]
	    arr2=[]
	    arr3=[]
	    for i in arr:
	        if i<a:
	            arr1.append(i)
	        elif i>b:
	            arr3.append(i)
	        else:
	            arr2.append(i)
	    arr.clear()
	    arr.extend(arr1)
	    arr.extend(arr2)
	    arr.extend(arr3)
