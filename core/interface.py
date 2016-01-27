from core.functions import *
from unicurses import *

KEY_ENTER = 10;

def print_menu(wins, highlight, choices):
	wclear(wins["menu"]["win"]);
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
	game_info = {};
	game_info["lvl"] = "";
	game_info["difficulty"] = 1;
	game_info["multiplier"] = 1;
	game_info["quit"] = False;

	wins["menu"]["win"] = add_win( wins["menu"] );

	highlight = 1;
	step = 0;

	while (True):
		if (step == 0):
			choices = ["Start game", "Quit"];
		elif (step == 1):
			choices = ["Level 1", "Level 2"];
		elif (step == 2):
			choices = ["Easy", "Medium", "Hard"];

		n_choices = len(choices)

		while ( True ):
			choice = "";

			print_menu(wins, highlight, choices);

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
				choice = choices[highlight - 1];
				wrefresh(wins["menu"]["win"]);


			if (choice == "Start game"):
				highlight = 1;
				break;

			elif (choice == "Quit"):
				game_info["quit"] = True;
				break;

			elif (choice == "Level 1"):
				highlight = 1;
				game_info["lvl"] = "lvl_1";
				break;

			elif (choice == "Level 2"):
				highlight = 1;
				game_info["lvl"] = "lvl_2";
				break;

			elif (choice == "Easy"):
				game_info["difficulty"] = 0.12;
				game_info["multiplier"] = 2;
				break;

			elif (choice == "Medium"):
				game_info["difficulty"] = 0.08;
				game_info["multiplier"] = 4;
				break;

			elif (choice == "Hard"):
				game_info["difficulty"] = 0.05;
				game_info["multiplier"] = 6;
				break;

		if (step == 2 or game_info["quit"] == True):
			del_win(wins["menu"]["win"]);
			break;

		step += 1;

	return game_info;