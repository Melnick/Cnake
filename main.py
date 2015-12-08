# from unicurses import *
from time import *
from random import *

from cnake import *
from food import *
# from functions import *s

# Coords format - (y, x)
START_COORDS = (2, 2);


def main():
	stdscr = initscr()

	screen_resolution = [(0, 0), getmaxyx(stdscr)];
	start_coords = get_mid( screen_resolution, (-5, -30) );

	# mvaddstr(6, 5, screen_resolution )


	noecho()
	curs_set(0)
	keypad(stdscr, True)
	nodelay(stdscr, True)

	border()

	cnake = Cnake( start_coords );
	food = Food( screen_resolution );
	food.spawn();
	render( food.food );

	while ( True ):
		cnake.del_dead_tail();


		for i in range( len(cnake.body) ):
			render( [cnake.TAIL_CH, (cnake.body[i][0], cnake.body[i][1])] );
		render( [cnake.HEAD_CH, (cnake.head[0], cnake.head[1])] );



		c = getch()

		if   ( c == KEY_LEFT  and not cnake.to_vector('r') ):
			cnake.vector = cnake.direction['l'];

		elif ( c == KEY_RIGHT and not cnake.to_vector('l') ):
			cnake.vector = cnake.direction['r'];

		elif ( c == KEY_UP    and not cnake.to_vector('b') ):
			cnake.vector = cnake.direction['t'];

		elif ( c == KEY_DOWN  and not cnake.to_vector('t') ):
			cnake.vector = cnake.direction['b'];


		cnake.move();

		p = mvinch(cnake.head[0], cnake.head[1]);
		if ( p != ord(' ') and chr(p) in Food.foods):
			food.spawn();
			render( food.food );
			cnake.add_body();
		elif ( p != ord(' ') ):
			cnake.dead = True;


		if ( cnake.dead ):
			break;

		refresh()
		sleep(0.05)

	mvaddstr(6, 5, food.food)








try:
	main();
except Exception as e:
	clear();
	refresh();
	print( "{0}".format(e) );

	f = open("last.log", "w");
	f.write( "{0}".format(e) );
	f.close();

	f = open("all.log", "a+");
	f.write( "{0}\n\n".format(e) );
	f.close();


# End
while ( True ):
	c = getch()
	if ( c == ord('q') ):
		clear();
		refresh();
		break;
endwin()