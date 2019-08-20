from chef import Chef
import random
from collections import namedtuple

w_chef = namedtuple('w_chef', 'since chef')

class Scheduler:

	def __init__(self):
		self.chefs_main = []
		self.chefs_side = []
		self.schedule = [None] * Chef.days_in_week * 3
		#self.last_week = []
		#self.day_buffer = 4
		#self.must_cook_days = 2
		#self.cancelled = [] # list of days no one should cook; 1 = Monday, 2 = Tuesday, ... 7 = Sunday

	# Public Methods ####################################################################

	def add_chef(self, chef, main=True):
		if (main):
			self.chefs_main.append(chef)
		else:
			self.chefs_side.append(chef)

	def schedule_three_weeks(self):
		for day, sched in enumerate(self.schedule):
			self._schedule_day(day)

	def print_schedule(self):
		print("\n      Main   | Side\n________________________")
		for i, day in enumerate(self.schedule):
			if (day):
				print(self._day_of_week(i) + str(day[0]) + "|" + str(day[1]))
			else:
				print(self._day_of_week(i) + "Nobody cooks")
			if (i % Chef.days_in_week == Chef.days_in_week - 1):
				print("")
		print("")

	# Private Methods ###################################################################

	"""
	Schedule one day given the chefs, their availability and cooking record, and what day it is today.
	day: int < 14
	"""
	def _schedule_day(self, day):
		(main, side) = self._choose(day)
		self.schedule[day] = (main, side)

		for chef in self.chefs_main:
			if main:
				if (chef.name == main.name):
					chef.cook(day)
				else:
					chef.dont_cook()

		for chef in self.chefs_side:
			if side:
				if (chef.name == side.name):
					chef.cook(day)
				else:
					chef.dont_cook()

	def _get_sorted_map(self, list_of_chefs):
		get_tuple = lambda chef: w_chef(chef.since, chef)
		weights_s = list(map(get_tuple, list_of_chefs))
		weights_s.sort(reverse=True, key=lambda tup: tup.since)
		return weights_s

	def _find_available_chef(self, sorted_chefs, day):
		# sorted_chefs: a reverse-sorted list of w_chef objects (chef.since, chef)
		current_day = day % Chef.days_in_week
		for (since, chef) in sorted_chefs:
			if current_day not in chef.unavailable:
				return chef
		return None

	def _choose(self, day):
		weights_m = self._get_sorted_map(self.chefs_main)
		main = self._find_available_chef(weights_m, day)

		weights_s = self._get_sorted_map(self.chefs_side)
		weights_s = list(filter(lambda weight_chef: weight_chef.chef.name != main.name, weights_s))
		side = self._find_available_chef(weights_s, day)

		return (main, side)

	def _day_of_week(self, day):
		day = (day) % Chef.days_in_week
		name = ""
		if (day == 0):
			name = "Sun"
		if (day == 1):
			name = "Mon"
		if (day == 2):
			name = "Tue"
		if (day == 3):
			name = "Wed"
		if (day == 4):
			name = "Thu"
		# if (day == 5):
		# 	name = "Fri"
		# if (day == 6):
		# 	name = "Sat"
		return name + ": "

	"""
	def next_week(self):
		pass
	"""



