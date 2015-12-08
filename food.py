from random import *
from functions import *

class Food():

	foods = ['*', 'o', '%'];
	scr_res = [];
	food_coord = (5, 5);
	food = [];

	def __init__(self, screen_resolution):
		self.scr_res = screen_resolution;

	def spawn(self):
		r = [ add_vector(self.scr_res[0], (+1, +1))
		    , add_vector(self.scr_res[1], (-2, -2)) ];

		self.food_coord = ( randint( r[0][0], r[1][0] )
		                  , randint( r[0][1], r[1][1] ) );

		# f = open("coords.log", "a+");
		# for i in range(1000):
		# 	self.food_coord = ( randint( r[0][0], r[1][0] )
		#                       , randint( r[0][1], r[1][1] ) );
		# 	f.write( "{0}\n".format( self.food_coord ) );
		# f.close();

		self.food = [self.foods[randint(0, 2)], self.food_coord];