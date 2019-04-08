import libtvs
from libtvs import green

class person:
	name=''
	unreaded=''
	history=''
	todo=''
	lastans=''
	respect=''
	def __init__(self, name, unreaded, history, todo, lastans, respect):
		self.name=name
		self.unreaded=unreaded
		self.history=history
		self.todo=todo
		self.lastans=lastans
		self.respect=respect

sunshine=person('sunshine',None,None,None,None,0)
artem=person('artem',None,None,None,None,0)

def viewhistory(fromwho):
	print('\n========================================')
	print(eval(fromwho).history)
	print('======================================== \n')

def viewmessage(fromwho):
	try:

		if eval(fromwho).unreaded != None:
			print(eval(fromwho).unreaded)

			try:
				eval(fromwho).history=eval(fromwho).history + '\n' + eval(fromwho).unreaded
			except TypeError:
				eval(fromwho).history=eval(fromwho).unreaded
			eval(fromwho).unreaded=None
			a=(eval(fromwho).todo)
			print(' ')
			ans=(eval(a))
			eval(fromwho).todo=None
			return ans
			
		else:
			print('empty')
	except NameError:
		print('error03: ' + fromwho + ': no such person')
# нивкакиекавычки

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
			you=green('You') + (': ')
			eah=eval(asking).history
			eval(asking).history=(str(eah) + '\n' + str(you) +  str(answers[0]))
			eval(asking).lastans=1
			return 1
		elif callback == "2":
			you=green('You') + (': ')
			eah=eval(asking).history
			eval(asking).history=(str(eah) + '\n' + str(you) +  str(answers[1]))
			eval(asking).lastans=2
			return 2
		else:
			print(libtvs.red('\'' + callback + "\': is not right number, yeah?"))

