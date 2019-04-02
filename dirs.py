class dir:
	name = ""
	subdirs = []
	files = []
	def __init__(self, name, subdirs, files):
		self.name = name
		self.subdirs = subdirs
		self.files = files		

class file:
	name = ""
	content = ""
	type = ""
	def __init__(self, name, content, type):
		self.name = name
		self.content = content
		self.type = type
# Files initialization

readme = file("readme.txt", "this is file for test bla-bla-bla", "txt") 

# Directories initialization sub --> parents

userdir = dir("~", [], [readme])
home = dir("home", [userdir], [])

root = dir("/", [home], []) # Always at the end
