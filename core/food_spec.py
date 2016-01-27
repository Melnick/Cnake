from random import *

from core.functions import *

class Food_spec():

	colors = [];
	foods = [];
	area = [];
	coords = ();
	tmp = [];
	color = 0;
	c = 0;
	live = False;
	step = 0;
	max_step = 0;

	def __init__(self, wins, border):
		self.wins = wins;

		h = self.wins["arena"]["h"];
		w = self.wins["arena"]["w"];
		self.tmp = [(y, x) for y in range( h ) for x in range( w )]

		self.area = list(set(self.tmp) - set(border));

		self.foods = ['*', 'o', '%', '&', '$', '#', 'G', 'W'];
		self.colors = [COLOR_CYAN, COLOR_MAGENTA, COLOR_YELLOW
		              , COLOR_BLUE, COLOR_GREEN, COLOR_RED];
		self.c = CCHAR( self.foods[0] );
		self.color = self.colors[0];
		self.max_step = 120;

	def spawn(self, cnake):
		self.live = True;
		self.step = self.max_step;

		r = list( set(self.area) - set(cnake.body) - set(cnake.head));

		if (len(r) != 0):
			self.coords = r[randint( 0, len(r) - 1 )];
			self.color = self.colors[randint( 0, len(self.colors) - 1 )];
			self.c = CCHAR( self.foods[randint(0, len(self.foods) - 1)] );
		else:
			self.coords = None;

