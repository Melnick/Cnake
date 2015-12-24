import os
import shutil

from unicurses import *
from appdirs import *


SEPARATOR = (os.name in ['ce', 'nt', 'dos']) and '\\' or '/';


def add_vector(a, b):
	return (a[0] + b[0], a[1] + b[1]);


def w_log( path, attr = "a+", string = '' ):
	dir_path = user_log_dir("cnake");
	path = "{}{}{}".format(dir_path, SEPARATOR, path);

	if (not os.path.isdir( dir_path )):
		os.makedirs( dir_path );

	f = open(path, attr);
	f.write(string);
	f.close();


def rm_log_dir():
	path = user_log_dir("cnake");

	# try 0
	# for i in os.walk(path):
	# 	# print(i)
	# 	for j in i[2]:
	# 		file = "{}{}{}".format(i[0], SEPARATOR, j);
	# 		if os.path.isfile(file):
	# 			os.unlink(file);
	# 		# print(file)

	# try 1
	# if (os.path.isdir( path )):
	# 	shutil.rmtree( '{0}{1}..{1}..{1}'.format(path, SEPARATOR) );

	# try 2
	path = "{}{}".format(path[:path.find('cnake'):], "cnake");
	if (os.path.isdir( path )):
		shutil.rmtree( path );


def add_win( win ):
	return newwin(win['h'], win['w'], win["start_y"], win["start_x"]);

def del_win( win ):
	wclear(win);
	wrefresh(win)
	delwin(win);