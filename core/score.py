class Score():
	score = 0;
	score_food = 0;
	score_spec = 0;
	multiplier = 1;

	def __init__(self, difficulty_multiplier, lvl_multiplier):
		self.multiplier = difficulty_multiplier + lvl_multiplier;

	def add(self, num, spec = False):
		if (spec == False):
			self.score_food += num;
		else:
			self.score_spec += num;

		self.score = self.score_food * self.multiplier + self.score_spec;