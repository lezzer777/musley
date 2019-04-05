import libtvs

class somebody:
	name=''
	unreaded=''
	history=''
	todo=''
	def __init__(self, name, unreaded, history, todo):
		self.name=name
		self.unreaded=unreaded
		self.history=history
		self.todo=todo

test=somebody('sunshine',None,None,None)

def viewhistory(fromwho):
	print('========================================')
	print(eval(fromwho).history)

def viewmessage(fromwho):
	if eval(fromwho).unread != None:
		print(eval(fromwho).unread)

		if eval(fromwho).todo != None:
			c=eval(fromwho).todo
			eval(c)
			eval(fromwho).todo=None

		try:
			eval(fromwho).history=eval(fromwho).history + '\n' + eval(fromwho).unread
		except TypeError:
			eval(fromwho).history=eval(fromwho).unread
		eval(fromwho).unread=None
	else:
		print('empty')

def say(name, phrase):
	print(libtvs.blue(name) + ": " + phrase)

def notify(name, phrase, todo):
	
	print("You have an unread message from: " + libtvs.blue(eval(name).name) + 'type \'qms view [' + eval(name).name + ']\' to open message')
	eval(name).unread=(libtvs.blue(eval(name).name) + ": " + phrase)
	eval(name).todo=todo

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

