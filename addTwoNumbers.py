#addTwoNumbers.py
'''
Description:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
'''

class addTwoNumbers():
	def __init__(self, value, nextNode = None):
		self.value = value
		self.nextNode = nextNode

	def addNodes(self, node1, node2):
		carry = 0
		currentNode1 = node1
		currentNode2 = node2

		the_sum_of_values = self.addingValues(currentNode1, currentNode2)
		carry =  the_sum_of_values // 10
		if carry > 0:
			sumNode = addTwoNumbers(the_sum_of_values%10)
		else:
			sumNode = addTwoNumbers(the_sum_of_values)

		if currentNode1.nextNode is not None and currentNode2.nextNode is not None:
			currentNode1 = currentNode1.nextNode
			currentNode2 = currentNode2.nextNode

			currentNode1.value = currentNode1.value + carry #adding the carried number to the value

			returnedNode = self.addNodes(currentNode1, currentNode2)
			sumNode.nextNode = returnedNode
		elif currentNode1.nextNode is None and currentNode2.nextNode is not None:
			currentNode2.value = currentNode2.value + carry
		elif currentNode2.nextNode is None and currentNode1.nextNode is not None:
			currentNode1.value = currentNode1.value + carry

		return sumNode
		

	def addingValues(self, node1, node2):
		the_sum_of_values = node1.value + node2.value
		return the_sum_of_values

node_one_list_one = addTwoNumbers(2)
node_two_list_one = addTwoNumbers(4)
node_three_list_one = addTwoNumbers(3)

node_one_list_one.nextNode = node_two_list_one
node_two_list_one.nextNode = node_three_list_one

node_one_list_two = addTwoNumbers(5)
node_two_list_two = addTwoNumbers(6)
node_three_list_two = addTwoNumbers(4)

node_one_list_two.nextNode = node_two_list_two
node_two_list_two.nextNode = node_three_list_two

sumNode = node_one_list_one.addNodes(node_one_list_one, node_one_list_two)