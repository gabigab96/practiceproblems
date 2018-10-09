#parenthesisChecker.py


class parenthesisChecker():
	def __init__(self):
		text = "{([])}"
		result = self.checkForParenthesis(text)
		print(result)

		text2 = "()"
		result2 = self.checkForParenthesis(text2)
		print(result2)

		text3 = "}{([])}"
		result3 = self.checkForParenthesis(text3)		
		print(result3)

	def checkForParenthesis(self, text):
		openedCurly = 0
		closedCurly = 0
		openedParen = 0
		closedParen = 0
		openedBrac = 0
		closedBrac = 0

		for i in text:
			if '{' in i:
				openedCurly += 1
			elif '(' in i:
				openedParen += 1
			elif '[' in i:
				openedBrac += 1
			elif '}' in i:
				closedCurly +=1
			elif ')' in i:
				closedParen +=1
			elif ']' in i:
				closedBrac +=1

		if openedBrac is closedBrac and openedParen is closedParen and openedCurly is closedCurly:
			return "balanced"
		else:
			return "unbalanced"

alg = parenthesisChecker()