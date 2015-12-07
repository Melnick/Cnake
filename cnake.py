from unicurses import *
from food import *

class Cnake():

	'''
	l - left
	r - right
	t - top
	b - bot
	'''
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
		self.head = self.add_vector(self.head, self.vector);
		self.dead_tail = self.body[-1];

		for i in range(len(self.body) - 1, 0, -1):
			self.body[i] = self.body[i - 1];

		p = mvinch(self.head[0], self.head[1]);
		if ( p != ord(' ') and chr(p) in Food.foods):
			food = Food();
			food.spawn();
			self.add_body();
		elif ( p != ord(' ') ):
			self.dead = True;

	def render_cnake(self):
		for i in range( len(self.body) ):
			mvaddch(self.body[i][0], self.body[i][1], CCHAR('+'))
		mvaddch(self.head[0], self.head[1], CCHAR('@'))


	def del_dead_tail(self):
		if (self.dead_tail not in self.body):
			mvaddch(self.dead_tail[0], self.dead_tail[1], CCHAR(' '))

	def add_body(self):
		self.body.append(self.body[-1]);

	def to_vector( self, v ):
		if ( self.vector == self.direction[v] ):
			return True;
		return False;

	# @staticmethod
	def add_vector(self, a, b):
		return (a[0] + b[0], a[1] + b[1]);