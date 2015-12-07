from unicurses import *
from time import *
from random import *

from cnake import *
from food import *

# Coords format - (y, x)


stdscr = initscr()

dims = getmaxyx(stdscr);

noecho()
curs_set(0)
keypad(stdscr, True)
nodelay(stdscr, True)

cnake = Cnake((2, 2));

border()

food = Food();

while ( True ):
	cnake.del_dead_tail();
	cnake.render_cnake();

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

	if ( cnake.dead ):
		break;

	refresh()
	sleep(0.1)

# mvaddstr(6, 5, head)


# End
while ( True ):
	c = getch()
	if ( c == ord('q') ):
		clear();
		refresh();
		break;
endwin()