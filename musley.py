from termcolor import colored
import dirs
import sys
import re

session = {
	"user": "user",
	"cur_dir": dirs.userdir
}

comd = ""

def findCommand(command, tofind):
	if re.search(tofind, command):
		command = command.replace(tofind, "")
		command = command.replace(" ", "")
		return command

while True:
	try:
		comd = input("[" + session["user"] + colored("@", "red") + "pc] ")
	except KeyboardInterrupt:
		print("please, use exit command to exit.")

	if comd == "exit":
		sys.exit("Goodbye, " + session["user"])

	if findCommand(comd, "ls") != None:
		for file in session["cur_dir"].files:
			print(file.name)
		for subdir in session["cur_dir"].subdirs:
			print(colored(subdir.name, "blue"))
	 