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



# class Food():

# 	foods = ['*', 'o', '%'];
# 	area = [];
# 	food_coord = (1, 1);
# 	item = {};

# 	def __init__(self, wins):
# 		self.wins = wins;

# 		for y in range( self.wins["arena"]["h"] ):
# 			for x in range( self.wins["arena"]["w"] ):
# 				if not ( x == 0
# 				      or y == 0
# 				      or x == self.wins["arena"]["h"] - 1
# 				      or y == self.wins["arena"]["h"] - 1):
# 					self.area.append( (y, x) );

# 	def spawn(self, cnake):
# 		h = self.wins["arena"]["h"];
# 		w = self.wins["arena"]["w"];

# 		r = [(y, x) for y in range(h) for x in range(w) if (y, x) not in cnake and (y, x) in self.area];

# 		self.food_coord = r[randint( 0, len(r) - 1 )];

# 		self.item = { 'y': self.food_coord[0], 'x': self.food_coord[1], 'c': CCHAR( self.foods[randint(0, 2)] )};


