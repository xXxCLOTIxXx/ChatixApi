import random

def generateUid(amount: int = 8):
	code = ""
	for x in range(amount):
		for i in range(amount):
			code = code + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
		code = code+'-'

	return code