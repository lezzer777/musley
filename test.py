import dialogus
from libtvs import *
import re
from os import system

def fc(command, tofind):
	if re.search(tofind, command):
		command = command.replace(tofind, "")
		#command = command.replace('recieve', "")
		command = command.replace("", "")
		return command
		
def fcantire(command, tofind):
	if re.search(tofind, command):
		command = command.replace(tofind, "")
		command = command.replace('recieve', "")
		command = command.replace(" ", "")
		return command

print(yellow('=============================='))
print(yellow('dialogus develooper console v2'))
print(yellow('=============================='))

# exec dialogus.notify('test','hello','menu([\'aaa\',\'bbbb\'],\'test\')')
# exec dialogus.viewmessage('test')



while True:
	quest=input(red('[') + blue('dev@https://github.com/lezzer777/musley/') + red(']') + blue('->'))
	
	if fc(quest,'reboot') != None:
		system('python test.py')
	elif fc(quest,'exit') != None:
		s1=fc(quest,'exit')
		print('logout()')
		exit(s1)
	elif fc(quest,'exec') != None:
		s1=fc(quest,'exec')
		print('BE CAREFUL WITH EXEC')
		eval(s1)
	elif fc(quest,'dialog') != None:
		s1=fc(quest,'dialog')
		if s1 == fc(quest,'recieve'):
			s2=fc(s1,'recieve')
			s2=fcantire(s2,'recieve')
			if s2 == '-h' or s2 == '--help' or s2 == None or s2 == '' or s2 == ' ' or s2 == '  ':
				print('''
dialogus.notify (dialog recieve) USAGE:
		dialog recieve from_who(person.name),phraze,what_need_to_do_after_showing_bessage
	EXAMPLE:
		dialog recieve test,'hello',menu(['lol','kek'])
				''')
			dialogus.notify(exec(s2))
		else:
			print('unsupported argument: ' + s1)
	else:
		print('e01: \'' + quest + '\': no such command')
		
