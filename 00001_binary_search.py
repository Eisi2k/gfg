class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
        if k in arr:
            x = list(arr)
            y = x.index(k)
            return y
        else:
            return -1 #k not included in array
