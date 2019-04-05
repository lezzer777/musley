#!/bin/env python3
#test
from time import sleep
from termcolor import colored
from libtvs import logo, clear
import dirs
import sys
from os import system, name
import re
import dialogus
# import initanim # убрать на время разработки
import libsoft
import datetime

def welcome():
	print('Welcome to ' + red('BlackArch'))
	dialogus.say('qms-service','qms-service ready to recieve messages')

clear()
logo()

session = {
	"user": None,
	"cur_dir": None
}

class user:
	name = ""
	password = ""
	homedir = None

	def __init__(self, name, password, homedir):
		self.name = name
		self.password = password
		self.homedir = homedir

mainuser = user("anon", "passwd", dirs.userdir)
root = user("root", "toor", dirs.rootUserDir)

users = [mainuser, root]

comd = ""
def panc(w):
	global pan
	pan=True

def red(what):
	a=colored(what,'red')
	return a
def blue(what):
	a=colored(what,'blue')
	return a
def green(what):
	a=colored(what,'green')
	return a
def yellow(what):
	a=colored(what,'yellow')
	return a
def purple(what):
	a=colored(what,'magenta')
	return a
	

def findCommand(command, tofind):
	if re.search("^" + tofind, command):
		command = command.replace(tofind, "")
		command = command.replace(" ", "")
		return command
aba=0
pan=False
while session["user"] == None:
	input_login = input("musley login: ")
	input_password = input(input_login + "\'s password: ")
	for user in users:
		
		
		if input_login == user.name and input_password == user.password:
			sleep(1)
			pan=True
			session["user"] = user
			session["cur_dir"] = user.homedir
			pan=True
			panc(1)
			welcome()
		if pan:
			sleep(0.02)
		else:
			if aba == 0:
				sleep(1)
				print('System error.')
				aba=1
			else:
				print('try again')
				aba=0


while True:
	try:
		if session["cur_dir"].name == 'anon':
			cdn='~'
		else:
			cdn=session["cur_dir"].name
			dialogus.notify('test','it\'s a beta','menu([\'yeah, i know\',\'i know (2)\'],\'test\')')
		
		comd = input(red("[") + yellow(session["user"].name) + green('@') + blue("musley ") + purple(cdn) + red("]") + "$ ")
	except KeyboardInterrupt:
		print("please, use exit command to exit.")

	if findCommand(comd, 'exit') != None:
		sys.exit("Goodbye, " + session["user"].name)

	elif findCommand(comd, "ls") != None:
		for subdir in session["cur_dir"].subdirs:
			print(colored(subdir.name, "blue"))
		for file in session["cur_dir"].files:
			print(file.name)

	elif findCommand(comd, "pwd") != None:
		print(session["cur_dir"].name)

	elif findCommand(comd, "cat") != None:
		for subfile in session["cur_dir"].files:
			if subfile.name == findCommand(comd, "cat"):
				print(subfile.content)
	elif findCommand(comd, "cd") != None:
		if comd == "cd ../" or comd == "cd ..":
			for path in dirs.paths:
				if session["cur_dir"] in path.subdirs:
					session["cur_dir"] = path

		else:
			for subdir in session["cur_dir"].subdirs:
				try:
					if ac:
						sleep(0.01)
					else:
						ac=False
				except NameError:
					ac=False
						
				ac=False
				if findCommand(comd, "cd") == subdir.name:
					session["cur_dir"] = subdir
					ac=True
			if ac:
				sleep(0.01)
			else:
				sleep(0.01)
#				print('error. \'' + findCommand(comd, "cd") + '\' not found')


	elif findCommand(comd, 'echo') != None:
		print(findCommand(comd, 'echo'))
	
	elif findCommand(comd, "clear") != None:
		if name == "nt":
			system("cls")
		else:
			system("clear")

	elif findCommand(comd, "whoami") != None:
		print(session["user"].name)


	elif findCommand(comd, "nmap") != None:
		s1=findCommand(comd, "nmap ")
		if comd == 'nmap' or comd == 'nmap ' or comd == 'nmap  ':
			print('''
e01: option needed

EXAMPLES:
  nmap -On tvsclass.github.io
SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES ''')
		else:

			if findCommand(s1, "-On"):
				ip=findCommand(s1, "-On")
				libsoft.nmap(ip)
			else:
				date=datetime.date.today()
				print('''Starting Nmap 7.70 ( https://nmap.org ) at ''' + str(date) + '''
Failed to resolve \'''' + s1 + '''\'
WARNING: No targets were specified, so 0 hosts scanned.
Nmap done: 0 IP addresses (0 hosts up) scanned in 0.15 seconds ''')

	elif findCommand(comd, "qms") != None:
		s1=findCommand(comd, "qms")
		if findCommand(s1, "view") != None:
			s2=findCommand(s1, "view")
			ans=dialogus.viewmessage(s2)
		elif findCommand(s1, "history") != None:
			s2=findCommand(s1, "history")
			ans=dialogus.viewhistory(s2)
		else:
			print(s1 + ': option not found')

	else:
		if comd == None or comd == ' ' or comd == '  ':
			sleep(0.0001)
		elif comd == '':
			sleep(0.0001)
		else:
			print(comd + ': command not found')


