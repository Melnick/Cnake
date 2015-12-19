from core.food import *
from core.functions import *

class Cnake():

	HEAD_CH = CCHAR('@');
	TAIL_CH = CCHAR('+');
	VOID_CH = CCHAR(' ');


	# l - left
	# r - right
	# t - top
	# b - bot
	direction = {
		'l': (+0, -1),
		'r': (+0, +1),
		't': (-1, +0),
		'b': (+1, +0)
	}

	vector = direction['r'];

	def __init__(self, coords):
		self.head = coords;
		self.body = [self.head[:]] * 5;
		self.dead_tail = self.body[-1];
		self.dead = False;



	def move(self):
		self.body[0] = self.head;
		self.head = add_vector(self.head, self.vector);
		self.dead_tail = self.body[-1];

		for i in range(len(self.body) - 1, 0, -1):
			self.body[i] = self.body[i - 1];

	def add_body(self):
		for i in range(1):
			self.body.append(self.body[-1]);

	def to_vector( self, v ):
		if ( self.vector == self.direction[v] ):
			return True;
		return False;