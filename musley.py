#!/bin/env python3
#test
from time import sleep
from termcolor import colored
from libtvs import logo, clear
import dirs
import sys
from os import system, name
import re

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

while session["user"] == None:
	input_login = input("musley login: ")
	input_password = input(input_login + "\'s password: ")

	for user in users:
		global pan
		pan=False
		if input_login == user.name and input_password == user.password:
			sleep(1)
			pan=True
			session["user"] = user
			session["cur_dir"] = user.homedir
			pan=True

	if pan:
		sleep(0.01)
	
while True:
	try:
		if session["cur_dir"].name == 'anon':
			cdn='~'
		else:
			cdn=session["cur_dir"].name

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
				if findCommand(comd, "cd") == subdir.name:
					session["cur_dir"] = subdir

	elif findCommand(comd, 'echo') != None:
		print(findCommand(comd, 'echo'))
	
	elif findCommand(comd, "clear") != None:
		if name == "nt":
			system("cls")
		else:
			system("clear")

	elif findCommand(comd, "whoami") != None:
		print(session["user"].name)


	else:
		if comd == None or comd == ' ' or comd == '  ':
			sleep(0.0001)
		elif comd == '':
			sleep(0.0001)
		else:
			print(comd + ': command not found')
