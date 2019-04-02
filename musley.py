from termcolor import colored
import dirs
import sys

session = {
	"user": "user",
	"cur_dir": dirs.userdir
}

while True:
	try:
		comd = input("[" + session["user"] + colored("@", "red") + "pc] ")
	except KeyboardInterrupt:
		print("please, use exit command to exit.")

	if comd == "exit":
		sys.exit("Goodbye, " + session["user"])