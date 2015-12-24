from core.functions import *
from unicurses import *

KEY_ENTER = 10;

def print_menu(wins, highlight, choices):
	n_choices = len(choices);
	y = int(wins["menu"]["h"] / 2 - n_choices / 2);

	for i in range(0, n_choices):
		x = int(wins["menu"]["w"] / 2 - len(choices[i]) / 2);

		if (highlight == i + 1):
			wattron(wins["menu"]["win"], A_REVERSE);
			mvwaddstr(wins["menu"]["win"], y, x, choices[i]);
			wattroff(wins["menu"]["win"], A_REVERSE);
		else:
			mvwaddstr(wins["menu"]["win"], y, x, choices[i]);
		y += 1;

	wrefresh(wins["menu"]["win"]);



def menu( wins ):
	gameover = False;

	wins["menu"]["win"] = add_win( wins["menu"] );

	highlight = 1;
	choice = 0;
	choices = ["Start game", "Quit"];
	n_choices = len(choices);
	print_menu(wins, highlight, choices);

	while ( True ):
		c = getch();
		if c == KEY_UP:
			if highlight == 1:
				highlight = n_choices;
			else:
				highlight -= 1;
		elif c == KEY_DOWN:
			if highlight == n_choices:
				highlight = 1;
			else:
				highlight += 1;
		elif c == KEY_ENTER:
			choice = highlight;
			wrefresh(wins["menu"]["win"]);

		print_menu(wins, highlight, choices);

		if (choice == 1):
			del_win(wins["menu"]["win"]);
			gameover = False;
			break;
		elif (choice == 2):
			del_win(wins["menu"]["win"]);
			gameover = True;
			break;

	return gameover;