#import tvslogo
from termcolor import colored
from os import system
import itertools
import time

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

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def ok(what):
	print('[' + green('OK') + '] ' + what)
def error(what):
	print('[' + red('ERROR') + '] ' + what)
def loading(what):
	print('[' + blue('***') + '] ' + what)
def wsnloading(what, t, r):
	print('[' + blue('***') + '] ' + what, end='')
	it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
	for x in range(r):
		time.sleep(t)
		print(next(it), end='', flush=True)
	print('\n')

def logo():
	print(red("""
@@  @@  @@  @@ @@@@@ @@   @@@@@ @@  @@
@@@@@@  @@  @@ @@    @@   @@     @  @
@@@@@@  @@  @@ @@@@@ @@   @@@@@   @@
@@  @@  @@  @@    @@ @@   @@      @@
@@  @@  @@@@@@ @@@@@ @@@@ @@@@@   @@

"""))
	print("""
======================================
by tvsclass & lezzer
======================================
""")
def clear():
	system('clear')

