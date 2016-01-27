from time import *
from random import *
from math import *

from unicurses import *

from core.cnake import *
from core.level import *
from core.score import *
from core.food import *
from core.food_spec import *
from core.functions import *
from core.interface import *


KEY_ESC = 27;

'''
    Score - 00000000                                                  @ - 10
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

	stdscr = initscr();
	cbreak();
	noecho();
	curs_set(0);
	keypad(stdscr, True);

	wrefresh(stdscr);


	crs_size = getmaxyx(stdscr);


	wins["status"]["h"] = 2;
	wins["status"]["w"] = crs_size[1];
	wins["status"]["start_y"] = 0;
	wins["status"]["start_x"] = 0;

	wins["arena"]["h"] = 23;
	wins["arena"]["w"] = crs_size[1];
	wins["arena"]["start_y"] = wins["status"]["h"];
	wins["arena"]["start_x"] = 0;

	wins["gameover"]["h"] = crs_size[0];
	wins["gameover"]["w"] = crs_size[1];
	wins["gameover"]["start_y"] = 0;
	wins["gameover"]["start_x"] = 0;

	wins["menu"]["h"] = crs_size[0];
	wins["menu"]["w"] = crs_size[1];
	wins["menu"]["start_y"] = 0;
	wins["menu"]["start_x"] = 0;

	gameover = False;

	while ( not gameover ):

		game_info = menu( wins );
		gameover = game_info["quit"];

		if ( not gameover ):
			wins["status"]["win"] = add_win( wins["status"] );
			wins["arena"]["win"]  = add_win( wins["arena"] );


			mvwaddstr(wins["status"]["win"], 0, 4, "Score - 00000000" );
			mvwaddstr(wins["status"]["win"], 1, 4, "Pause - p" );
			wrefresh(wins["status"]["win"]);

			lvl = Level(game_info["lvl"]);

			for coord in lvl.border:
				mvwaddstr(wins["arena"]["win"], coord[0], coord[1], ' ', A_REVERSE );

			wrefresh(wins["arena"]["win"]);


			score = game(wins, stdscr, lvl, game_info);


			del_win(wins["status"]["win"]);
			del_win(wins["arena" ]["win"]);

			wins["gameover"]["win"] = add_win( wins["gameover"] );

			string = "GAME OVER";
			x = int(wins["gameover"]["w"] / 2 - len(string) / 2);
			mvwaddstr(wins["gameover"]["win"], 11, x, string );

			string = "U score - {:0>8}".format(score);
			x = int(wins["gameover"]["w"] / 2 - len(string) / 2);
			mvwaddstr(wins["gameover"]["win"], 13, x, string );

			string = "Press ESC for quit game or M for game menu.";
			x = int(wins["gameover"]["w"] / 2 - len(string) / 2);
			mvwaddstr(wins["gameover"]["win"], 20, x, string );

			wrefresh(wins["gameover"]["win"])

			while ( True ):
				c = getch()
				if ( c == KEY_ESC ):
					gameover = True;
					break;

				elif ( c == CCHAR('m') or c == CCHAR('M')):
					del_win(wins["gameover"]["win"]);
					break;

	clear();
	refresh();
	endwin();


def game(wins, stdscr, lvl, game_info):

	nodelay(stdscr, True);

	start_coords = (2, 2);

	cnake = Cnake( start_coords );
	food = Food( wins, lvl.border );
	food.spawn( cnake );
	food_spec = Food_spec( wins, lvl.border );

	mvwaddch(wins["arena"]["win"], food.coords[0], food.coords[1], food.c);

	score = Score(game_info["multiplier"], lvl.multiplier);

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
			return score.score;

		elif ( c == CCHAR('p') or c == CCHAR('P') ):
			string = "PAUSE";
			x = int(wins["status"]["w"] / 2 - len(string) / 2);
			mvwaddstr(wins["status"]["win"], 1, x, string );
			wrefresh(wins["status"]["win"])
			nodelay(stdscr, False);
			while ( True ):
				ch = getch();

				if ( ch == CCHAR('p') ):
					nodelay(stdscr, True);
					mvwaddstr(wins["status"]["win"], 1, x, "     " );
					wrefresh(wins["status"]["win"])
					break;



		cnake.move();


		if (cnake.dead_tail not in cnake.body):
			mvwaddch(wins["arena"]["win"], cnake.dead_tail[0], cnake.dead_tail[1], CCHAR( cnake.VOID_CH ));


		for i in range( len(cnake.body) ):
			mvwaddch(wins["arena"]["win"],  cnake.body[i][0]
			       , cnake.body[i][1]
			       , CCHAR( cnake.TAIL_CH ) );


		mvwaddch(wins["arena"]["win"],  cnake.head[0]
		       , cnake.head[1]
		       , CCHAR( cnake.HEAD_CH ) );


		if (cnake.head in lvl.border or cnake.head in cnake.body):
			cnake.dead = True;
			break;

		elif (food.coords == cnake.head):
			score.add(1);
			food.spawn( cnake );
			cnake.add_body();
			if not (food.coords is None):
				mvwaddch(wins["arena"]["win"], food.coords[0], food.coords[1], food.c);

			if (food_spec.live == False and randint(0, 100) < 20):
				food_spec.spawn( cnake );
				if not (food_spec.coords is None):
					start_color();
					init_pair(1, food_spec.color, COLOR_BLACK);
					wattron(wins["arena"]["win"], COLOR_PAIR(1));
					mvwaddch(wins["arena"]["win"], food_spec.coords[0], food_spec.coords[1], food_spec.c);
					wattroff(wins["arena"]["win"], COLOR_PAIR(1));


		elif (food_spec.coords == cnake.head):
			score.add(10, True);
			cnake.add_body();
			food_spec.live = False;
			food_spec.step = 0;
			mvwaddstr(wins["status"]["win"], 0, 70, "       ");

		if (food_spec.live == True):
			food_spec.step -= 1;

			s = "{} - {: <3}".format(chr(food_spec.c), food_spec.step);

			start_color();
			init_pair(1, food_spec.color, COLOR_BLACK);
			wattron(wins["status"]["win"], COLOR_PAIR(1));
			mvwaddstr(wins["status"]["win"], 0, 70, s);
			wattroff(wins["status"]["win"], COLOR_PAIR(1));

			if (food_spec.step == 0):
				food_spec.live = False;
				mvwaddstr(wins["status"]["win"], 0, 70, "       ");
				mvwaddch(wins["arena"]["win"], food_spec.coords[0], food_spec.coords[1], CCHAR(' '));
				food_spec.coords = None;


		wrefresh(wins["arena"]["win"]);

		sleep(game_info["difficulty"]);

		mvwaddstr(wins["status"]["win"], 0, 12, "{:0>8}".format(score.score));
		wrefresh(wins["status"]["win"]);


	if ( cnake.dead ):
		string = "GAME OVER";
		x = int(wins["status"]["w"] / 2 - len(string) / 2);
		mvwaddstr(wins["status"]["win"], 1, x, string );
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

	nodelay(stdscr, False);
	return score.score;