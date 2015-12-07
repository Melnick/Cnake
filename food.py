from unicurses import *
from random import *

class Food():

	foods = ['*', 'o', '%'];

	def __init__(self, screen_resolution):
		self.spawn();
		self.render_food();
		self.scr_res = screen_resolution;

	def spawn(self):
		self.food = (randint(1, 23), randint(1, 78))

	def render_food(self):
		mvaddch(self.food[0], self.food[1], CCHAR(self.foods[randint(0, 2)]))