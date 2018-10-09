#reversedWord.py
#Given a String of length N reverse the whole string without reversing the individual words in it. Words are separated by dots.

class reversedWord():

	def __init__(self):
		words = "i.like.this.program.very.much"
		self.reverseWords(words)

		words2 = "pqr.mno"
		self.reverseWords(words2)

	def reverseWords(self, words):
		arr = words.split('.')
		words = ''
		for i in reversed(arr):
			words += i+'.'
		print(words)

alg = reversedWord()