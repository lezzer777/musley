class dir:
	name = ""
	subdirs = []
	files = []
	def __init__(self, name, subdirs, files):
		self.name = name
		self.subdirs = subdirs
		self.files = files		

# Directories initialization sub --> parents

userdir = dir("~", [], [])
home = dir("home", [userdir], [])

root = dir("/", [home], []) # Always at the end
