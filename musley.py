#!/bin/env python3

from termcolor import colored

import dirs
import sys
from os import system, name
import re

session = {
	"user": "somebody",
	"cur_dir": dirs.userdir
}

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

while True:
	try:
		comd = input(red("[") + yellow(session["user"]) + green('@') + blue("musley ") + purple(session["cur_dir"].name) + red("]") + "$ ")
	except KeyboardInterrupt:
		print("please, use exit command to exit.")

	if findCommand(comd, 'exit') != None:
		sys.exit("Goodbye, " + session["user"])

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
	
	elif findCommand(comd, "clear") != None:
		if name == "nt":
			system("cls")
		else:
			system("clear")

	elif findCommand(comd, "whoami") != None:
		print(session["user"])


	else:
		print(comd + ': command not found')
