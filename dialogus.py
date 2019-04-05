import libtvs
from libtvs import green

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
	print('\n ========================================')
	print(eval(fromwho).history)
	print('======================================== \n')

def viewmessage(fromwho):
	try:

		if eval(fromwho).unreaded != None:
			print(eval(fromwho).unreaded)
			print(eval(fromwho).name)
			if eval(fromwho).todo != None:
				c=eval(fromwho).todo
				eval(c)
				eval(fromwho).todo=None
			try:
				eval(fromwho).history=eval(fromwho).history + '\n' + eval(fromwho).unreaded
			except TypeError:
				eval(fromwho).history=eval(fromwho).unreaded
			eval(fromwho).unreaded=None
		else:
			print('empty')
	except NameError:
		print('error03: ' + fromwho + ': no such person')


def say(name, phrase):
	print(libtvs.blue(name) + ": " + phrase)

def notify(name, phrase, todo):
	print("You have an unread message from: " + libtvs.blue(eval(name).name) + '\n type \'qms view ' + eval(name).name + '\' to open message')
	eval(name).unreaded=(libtvs.blue(eval(name).name) + ": " + phrase)
	eval(name).todo=todo

def menu(answers, asking):
	for answer in answers:
		print(str(answers.index(answer) + 1) + ") " + answer)
	callback = ""
	while callback == "1" or callback != "2":
		callback = input("Answer: ")
		if callback == "1":
			you=green('You: ')
			eah=eval(asking).history
			eval(asking).history=(str(you) + str(eah) + str(answers[0]))
			return 1
		elif callback == "2":
			you=green('You: ')
			eah=eval(asking).history
			eval(asking).history=(str(you) + str(eah) + str(answers[1]))
			return 2
		else:
			print(libtvs.red("Not right number, yeah?"))

