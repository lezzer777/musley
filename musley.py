from termcolor import colored
import dirs

session = {
	"user": "user",
	"cur_dir": dirs.userdir
}


while True:
	comd = input("[" + session["user"] + colored("@", "red") + "pc] ")