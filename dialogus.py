import libtvs

def say(name, phrase):
	print(libtvs.blue(name) + ": " + phrase)

def notify(name, phrase):
	print("You have an unread message from: " + libtvs.blue(name))
	print(libtvs.blue(name) + ": " + phrase)

def menu(answers):
	for answer in answers:
		print(str(answers.index(answer) + 1) + ") " + answer)
	callback = ""
	while callback == "1" or callback != "2":
		callback = input("Answer: ")
		if callback == "1":
			return 1
		elif callback == "2":
			return 2
		else:
			print(libtvs.red("Not right number, yeah?"))

