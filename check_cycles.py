#check_cycles.py

class check_cycles():

	def __init__(self, value, nextNode = None):
		self.value = value
		self.nextNode = nextNode
		self.arr = []

	def check_linkedList(self, x):
		self.arr.append(x.value)

		if (x.nextNode).value in self.arr:
			return "cycle"
		elif x.nextNode is None:
			return "no cycle"
		else:
			result = self.check_linkedList(x.nextNode)
			return result

x = check_cycles(1)
x1 = check_cycles(2)
x2 = check_cycles(3)
x3 = check_cycles(4)

x.nextNode = x1
x1.nextNode = x2
x2.nextNode = x3
x3.nextNode = x1

result = x.check_linkedList(x)
print(result)
