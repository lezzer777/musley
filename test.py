import libtvs
import dialogus

def m():
	dialogus.menu(['hello','fuck you)'],'test')

libtvs.ok('ok')

dialogus.notify('test', 'hello', None)
dialogus.viewmessage('test')
dialogus.notify('test', 'hello', 'm()')

