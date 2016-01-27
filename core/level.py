import pickle

class Level():
	multiplier = 1;
	border = [];
	lvl_info = [];

	def __init__(self, level_name):

		f = open("core/data/{}.bin".format(level_name), "rb");
		self.lvl_info = pickle.load(f);
		f.close();

		self.multiplier = self.lvl_info[0];
		self.border = self.lvl_info[1];