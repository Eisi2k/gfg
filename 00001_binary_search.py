#easy search with index ;)

class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
        if k in arr:
            x = list(arr)
            y = x.index(k)
            return y
        else:
            return -1 #k not included in array

#binary search

def binary_search(arr, k):  # array, target

    low = 0  # left border
    high = len(arr) - 1  # right border
    mid = 0

    if len(arr) == 0:
        print("pls new array")

    while low <= high:

        # mean rounded down
        mid = (low + high) // 2

        if arr[mid] == k:
            return mid

        elif arr[mid] < k:
            low = mid + 1

        elif arr[mid] > k:
            high = mid - 1

    return -1


result = binary_search([1, 2, 3, 4, 5, 6, 7], 8)

if result == -1:
    print("no value")
else:
    print("Target is at index", result)
