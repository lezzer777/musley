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

# Actually, it's going to be in character's folder
docs = dir("Documents", [], [])
vids = dir("Videos", [], [])
pics = dir("Pictures", [], [])

userdir = dir("~", [docs, vids, pics], [])
rootUserDir = dir("root", [], [])
home = dir("home", [userdir], [])

root = dir("/", [home, rootUserDir], []) # Always at the end

paths = [root, home, userdir, docs]
