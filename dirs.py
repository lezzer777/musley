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
        r_path = ""
        def __init__(self, name, content, type, r_path):
                self.name = name
                self.content = content
                self.type = type
                self.r_path = r_path
# Files initialization

passwords = file("passwords.txt", "kavo:tavo", "txt", "https://kavo.com/passwords.txt")

# Directories initialization sub --> parents

# Actually, it's going to be in character's folder
docs = dir("Documents", [], [])
vids = dir("Videos", [], [])
pics = dir("Pictures", [], [])

userdir = dir('anon', [docs, vids, pics], [])
rootUserDir = dir("root", [], [])
home = dir("home", [userdir], [])
bin = dir("bin", [], [])  
etc = dir("etc", [], [])  
media = dir("media", [], []) 
proc = dir("proc", [], []) 
sbin = dir("sbin", [], [])   
sys = dir("sys", [], []) 
var = dir("var", [], [])
boot = dir("boot", [], []) 
mnt = dir("mnt", [], [])     
tmp = dir("tmp", [], [])
dev = dir("dev", [], [])  
lib = dir("lib", [], [])  
opt = dir("opt", [], [])   
run = dir("run", [], [])  
srv = dir("srv", [], [])    
usr = dir("usr", [], [])



root = dir("/", [home, rootUserDir, bin, etc, media, proc, sbin, sys, var, boot, mnt, tmp, dev, lib, opt, run, srv, usr], []) # Always at the end

paths = [root, home, userdir, docs]
