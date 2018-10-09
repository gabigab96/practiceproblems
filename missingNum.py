#missingNum.py
#Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.

class missingNum():

	def __init__(self):
		size = 5
		arr = [1, 2, 3, 5]
		result = self.findMissingNum(size, arr)
		print(result)
		
		size2 = 10
		arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
		result = self.findMissingNum(size2, arr2)
		print(result)
		
	def findMissingNum(self, size, arr):
		for i in range(size-1):
			expectedNum = i+1
			if arr[i] == expectedNum:
				continue
			else:
				return expectedNum
				break
		return size


alg = missingNum()