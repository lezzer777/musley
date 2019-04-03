from termcolor import colored
from os import system

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
def ok(what):
	print('[' + green(OK) + '] ' + what)
def error(what):
	print('[' + red(ERROR) + '] ' + what)
def logo():
	print(red("""
@@  @@  @@  @@ @@@@@ @@   @@@@@ @@  @@
@@@@@@  @@  @@ @@    @@   @@     @  @
@@@@@@  @@  @@ @@@@@ @@   @@@@@   @@
@@  @@  @@  @@ @@    @@   @@      @@
@@  @@  @@@@@@ @@@@@ @@@@ @@@@@   @@

"""))
	print("""
======================================
by tvsclass & lezzer
======================================
""")
def clear():
	system('clear')
