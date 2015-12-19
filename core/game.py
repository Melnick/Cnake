from time import *
from random import *
from math import *

from unicurses import *

from core.cnake import *
from core.food import *
from core.functions import *

KEY_ESC = 27;
DELAY = 0.1;

'''
    Score - 000000                                                    @ - 10
    Pause - p                      GAME OVER
+------------------------------------------------------------------------------+
'''

def game_init():

	wins = {
		"menu"    : {},
		"status"  : {},
		"arena"   : {},
		"gameover": {}
	};
	crs_size = {};


	stdscr = initscr()
	cbreak()
	noecho()
	curs_set(0)
	keypad(stdscr, True)

	wrefresh(stdscr);


	crs_size["stdsrc"] = getmaxyx(stdscr);
	crs_size["status"] = (2, crs_size["stdsrc"][1]);
	crs_size["arena"]  = ( crs_size["stdsrc"][0] - crs_size["status"][0]
		                 , crs_size["stdsrc"][1] )


	wins["status"]["h"] = crs_size["status"][0];
	wins["status"]["w"] = crs_size["status"][1];
	wins["status"]["start_y"] = 0;
	wins["status"]["start_x"] = 0;

	wins["status"]["win"] = add_win( wins["status"] );

	mvwaddstr(wins["status"]["win"], 0, 4, "Score - 000000" );
	mvwaddstr(wins["status"]["win"], 1, 4, "Pause - p [no work]" );
	wrefresh(wins["status"]["win"]);


	wins["arena"]["h"] = crs_size["arena"][0];
	wins["arena"]["w"] = crs_size["arena"][1];
	wins["arena"]["start_y"] = wins["status"]["h"];
	wins["arena"]["start_x"] = 0;

	wins["arena"]["win"] = add_win( wins["arena"] );

	box(wins["arena"]["win"], 0, 0)
	wrefresh(wins["arena"]["win"]);

	score = game(crs_size, wins, stdscr);

	del_win(wins["status"]["win"]);
	del_win(wins["arena" ]["win"]);


	wins["gameover"]["h"] = 25;
	wins["gameover"]["w"] = crs_size["stdsrc"][1];
	wins["gameover"]["start_y"] = 0;
	wins["gameover"]["start_x"] = 0;

	wins["gameover"]["win"] = add_win( wins["gameover"] );

	mvwaddstr(wins["gameover"]["win"], 11, 34, "GAME OVER" );
	mvwaddstr(wins["gameover"]["win"], 13, 30, "U score - {:0>6}".format(score) );
	mvwaddstr(wins["gameover"]["win"], 20, 20, "Press ESC for quit game or M for game menu." );
	wrefresh(wins["gameover"]["win"])


def game(crs_size, wins, stdscr):

	nodelay(stdscr, True);

	area = [(0, 1), crs_size["arena"]]
	start_coords = (2, 2);

	cnake = Cnake( start_coords );
	food = Food( area );
	food.spawn();

	mvwaddch(wins["arena"]["win"], food.item['y'], food.item['x'], food.item['c']);

	while ( True ):
		c = getch();

		if   ( c == KEY_LEFT  and not cnake.to_vector('r') ):
			cnake.vector = cnake.direction['l'];

		elif ( c == KEY_RIGHT and not cnake.to_vector('l') ):
			cnake.vector = cnake.direction['r'];

		elif ( c == KEY_UP    and not cnake.to_vector('b') ):
			cnake.vector = cnake.direction['t'];

		elif ( c == KEY_DOWN  and not cnake.to_vector('t') ):
			cnake.vector = cnake.direction['b'];

		elif ( c == KEY_ESC ):
			return 0;



		cnake.move();

		if (cnake.dead_tail not in cnake.body):
			mvwaddch(wins["arena"]["win"], cnake.dead_tail[0], cnake.dead_tail[1], CCHAR( cnake.VOID_CH ));


		for i in range( len(cnake.body) ):
			mvwaddch(wins["arena"]["win"],  cnake.body[i][0]
			       , cnake.body[i][1]
			       , CCHAR( cnake.TAIL_CH ) );

		p = mvwinch(wins["arena"]["win"], cnake.head[0], cnake.head[1]);

		mvwaddch(wins["arena"]["win"],  cnake.head[0]
		       , cnake.head[1]
		       , CCHAR( cnake.HEAD_CH ) );

		if ( p != ord(' ') and chr(p) in Food.foods):

			for i in range(100000):
				if (chr(mvwinch(wins["arena"]["win"], food.item['y'], food.item['x'])) != ' '):
					food.spawn();
				else:
					break;

			mvwaddch(wins["arena"]["win"], food.item['y'], food.item['x'], food.item['c']);

			cnake.add_body();

		elif ( p != ord(' ') ):
			cnake.dead = True;
			break;

		wrefresh(wins["arena"]["win"])

		sleep(DELAY)

		score = (len(cnake.body) - 5) * 7;
		mvwaddstr(wins["status"]["win"], 0, 12, "{:0>6}".format(score));
		wrefresh(wins["status"]["win"]);


	if ( cnake.dead ):
		mvwaddstr(wins["status"]["win"], 1, int(80 / 2 - 5), "GAME OVER" );
		wrefresh(wins["status"]["win"])

		for i in range(6):
			if (i % 2 != 0):
				for i in range( len(cnake.body) ):
					mvwaddch(wins["arena"]["win"], cnake.body[i][0], cnake.body[i][1], CCHAR( ' ' ));

				mvwaddch(wins["arena"]["win"], cnake.head[0], cnake.head[1], CCHAR( ' ' ));
			else:
				for i in range( len(cnake.body) ):
					mvwaddch(wins["arena"]["win"], cnake.body[i][0], cnake.body[i][1], CCHAR( cnake.TAIL_CH ));

				mvwaddch(wins["arena"]["win"], cnake.head[0], cnake.head[1], CCHAR( cnake.HEAD_CH ));

			wrefresh(wins["arena"]["win"])
			sleep(0.2)

	return score;