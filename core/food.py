from random import *

from core.functions import *

class Food():

	foods = [];
	area = [];
	coords = ();
	tmp = [];
	c = 0;

	def __init__(self, wins, border):
		self.wins = wins;

		h = self.wins["arena"]["h"];
		w = self.wins["arena"]["w"];
		self.tmp = [(y, x) for y in range( h ) for x in range( w )]

		self.area = list(set(self.tmp) - set(border));
		self.foods = ['*', 'o', '%', '&', '$', '#', 'G', 'W'];
		self.c = CCHAR( self.foods[0] );

	def spawn(self, cnake):
		r = list( set(self.area) - set(cnake.body) - set(cnake.head));

		if (len(r) != 0):
			self.coords = r[randint( 0, len(r) - 1 )];
			self.c = CCHAR( self.foods[randint(0, len(self.foods) - 1)] );
		else:
			self.coords = None;

