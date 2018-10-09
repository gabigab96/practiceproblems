#kadane_algorithm
#Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.

class kadane():
	def __init__(self):
		arr = [1,2,3]
		size = 3
		self.maxSum(arr, size)

		arr2 = [-1, -2, -3, -4]
		size2 = 4
		self.maxSum(arr2, size2)

	def maxSum(self, arr, size):
		findMax = arr

		if arr[0] > arr[1]:
			first = arr[0]
			second = arr[1]
		else:
			first = arr[1]
			second = arr[0]

		total_sum = first + second
		for i in range(2, size):
			if arr[i] > first:
				second = first
				first = arr[i]
			elif arr[i] > second and arr[i] != first:
				second = arr[i]

			total_sum += arr[i]

		findMax.append(total_sum)
		findMax.append(first + second)

		highestInMax = findMax[0]
		for i in range(1, len(findMax)):
			if findMax[i] > highestInMax:
				highestInMax = findMax[i]

		print(highestInMax)


alg = kadane()