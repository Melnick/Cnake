from unicurses import *


def add_vector(a, b):
	return (a[0] + b[0], a[1] + b[1]);

'''
param0 - [(start-y, start-x), (end-y, end-x)]
param1 - (offset-y, offset-x)
return - (mid-y, mid-x)
'''
def get_mid( yx, offset ):
	return ( int( (yx[1][0] - yx[0][0]) / 2 ) + offset[0], int( (yx[1][1] - yx[0][1]) / 2 )  + offset[1]);


'''
arrt - {}
'''

def render( attr ):
	mvaddch(attr[1][0], attr[1][1], CCHAR(attr[0]))
