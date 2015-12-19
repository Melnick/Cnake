from random import *

from core.functions import *

class Food():

	foods = ['*', 'o', '%'];
	scr = [];
	food_coord = (5, 5);
	item = {};

	def __init__(self, screen_size):
		self.scr = screen_size;

	def spawn(self):
		r = [ add_vector(self.scr[0], (+2, +2))
		    , add_vector(self.scr[1], (-3, -3)) ];

		self.food_coord = ( randint( r[0][0], r[1][0] )
		                  , randint( r[0][1], r[1][1] ) );

		self.item = { 'y': self.food_coord[0], 'x': self.food_coord[1], 'c': CCHAR( self.foods[randint(0, 2)] )};


