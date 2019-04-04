from libtvs import red, green, yellow, purple, blue
from libtvs import ok, error, loading, logo, wsnloading
from time import sleep
import itertools
from libtvs import clear

clear()

def probel(c):
	print('\n' * c)

logo()
a=('starting systemd kernel modules')
b=('starting tvs-m modules')
c=('starting qms service')
d=('starting login manager')




wsnloading(a, 0.5, 5)
ok(a)
probel(2)
wsnloading(b, 0.5, 5)
ok(b)
probel(2)
wsnloading(c, 0.5, 7)
ok(c)
probel(2)
wsnloading(d, 0.5, 4)
ok(d)
probel(1)
