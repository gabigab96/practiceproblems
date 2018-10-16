#median.py
import math

class median():
	def __init__(self):
		arr1 = [1,3,5]
		arr2 = [2,4,6]
		self.median = 0.0
		self.idx = 0.0

		self.combineArrays(arr1, arr2)

	def combineArrays(self, arr1, arr2):
		arr3 = []
		arr1_size = len(arr1)
		arr2_size = len(arr2)
		i = 0
		j = 0

		while i < arr1_size and j < arr2_size:
			if arr1[i] < arr2[j]:
				arr3.append(arr1[i])
				i += 1
			else:
				arr3.append(arr2[j])
				j += 1
		while i < arr1_size:
			arr3.append(arr1[i])
			i += 1
		while j < arr2_size:
			arr3.append(arr2[j])
			j += 1

		self.findMedian(arr3)

	def findMedian(self, arr3):
		size = len(arr3)

		if size%2 == 0:
			idx1 = int(size/2) -1 #subtract one because the indices star at 0
			idx2 = idx1+1
			total = arr3[idx1] + arr3[idx2]
			self.median = total/2
		else:
			self.idx = size/2
			self.idx = math.ceil(self.idx)
			self.median = arr3[self.idx]

		print(self.median)

alg = median()
