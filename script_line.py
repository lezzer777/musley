from libtvs import *
from time import sleep
from dialogus import *

# вообще можно сразу файл открыть в w потом в r, но я хочу фиолетовую надпись 

def savef(a_kuda,a_chto):
	saveW=open(a_kuda,'w')
	saveW.write(str(a_chto))
	saveW.close()

def loadrep(kavo):
	rep=open('.' + kavo,'r')
	eval(kavo).respect=rep.read()
	rep.close
	
def loadhistory(kavo):
	rep=open('.' + kavo + 'history','r')
	eval(kavo).history=rep.read()
	rep.close

def mnoty(who, phrase, ans1, ans2):
	notify(who,phrase,'menu([\'' + ans1 + '\',\'' + ans2 + '\'],\'' + who + '\')')
	#a= ('notify(' + str(who) + ',' + str(phrase) + ',' + 'menu([\'' + ans1 + '\',\'' + ans2 + '\']),\'artem\')')
	#eval(a)

loading('loading savefile...')
sleep(0.2)

try:
	saveR=open('.save','r')
	saveR.close()
	loadrep('NoName')
	loadhistory('NoName')

except FileNotFoundError:
	print(purple('creating savefile...'))
	savef('.save',0)

saveR=open('.save','r')

save=saveR.read()

try:
	save=int(save)
except ValueError:
	print(red('an error occurred while reading savefile (ETVS5_TRANSFORMTOINTERROR)'))
	error('load savefile')
	exit(5)

readed=False

print(green('save file loaded successfuly'))
ok('load savefile')



#########################################################
#                                                       #
#                ВОТ ЛИНЕЙНОСТЬ                  #
#                                                       #
#########################################################


def main():

	global readed

	global save

	if save == 0:
		if not readed:
			#notify('artem','hello','menu([\'hello\',\'who are you?\'],\'artem\')')
			mnoty('NoName','hello','hello','who are you?')
			readed=True
		else:
			save=1
			savef('.save',1)
			readed=False

	if save == 1:

		if NoName.lastans == 1:
			NoName.respect=1
		else:
			NoName.respect=0
		savef('.save',2)
		savef('.NoName',NoName.respect)
		savef('.NoNamehistory',NoName.history)
		
		
		
		
		
		
		
		
		
#                  КОНЕЦ ЛИНЕЙНОСТИ                           
###################################################################


