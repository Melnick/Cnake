import pickle

def main():

	while (True):
		s = input(">> ");

		if (s == "help"):
			print("Use format:");
			print("[lvl_name] [input_file] [multiplier]");
			s = '';
		else:
			lvl = s.split(' ');
			lvl_name = lvl[0];
			input_file = lvl[1];
			multiplier = int(lvl[2]);
			break;


	f = open("{}.dat".format(input_file), "r");

	border = [];

	for i in range(23):
		line = f.readline();

		for j in range(80):
			if (line[j] == "1"):
				border.append((i, j));

	f.close();

	lvl_info = [multiplier, border];


	f = open("{}.dat".format(lvl_name), "w");
	f.write(str(lvl_info));
	f.close();

	f = open("{}.bin".format(lvl_name), "wb");
	pickle.dump(lvl_info, f)
	f.close();


	print("Create file {}.bin | {} {}".format(lvl_name, input_file, multiplier))
	input("Press Enter for quit.");


if (__name__ == "__main__"):
	main();