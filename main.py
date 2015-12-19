import sys
import traceback

from core.game import *
from core.functions import *

# Coords format - (y, x)



def main():
	try:
		game_init();
	except Exception as e:
		exc_type, exc_value, exc_traceback = sys.exc_info();
		tb = traceback.format_exception(exc_type, exc_value, exc_traceback);
		string = ''.join(tb);
		w_log("last.log", "w", "game_init\n" + string + "\n\n");
		# w_log("logs.log", "a+", "{}\n\n".format(s));


	# End
	while ( True ):
		c = getch()
		if ( c == KEY_ESC ):
			clear();
			refresh();
			break;
	endwin()


if (__name__ == "__main__"):
	main();

	# try:
	# 	main();
	# except Exception as e:
	# 	exc_type, exc_value, exc_traceback = sys.exc_info();
	# 	tb = traceback.format_exception(exc_type, exc_value, exc_traceback);
	# 	string = ''.join(tb);
	# 	w_log("last.log", "a+", 'main\n' + string + "\n\n");