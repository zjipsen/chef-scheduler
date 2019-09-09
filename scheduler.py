from chef import Chef
import random
from collections import namedtuple

w_chef = namedtuple('w_chef', 'since chef')

class Scheduler:

	def __init__(self):
		self.chefs_main = []
		self.chefs_side = []
		self.schedule = [None] * 14

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

	def print_fairness(self):
		(main_unfair, side_unfair) = self._is_fair()
		print("\n_________________________________")
		print("Main unfairness: " + str(main_unfair))
		print("Side unfairness: " + str(side_unfair))

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
		self._print_chef_stats(day)

	def _get_sorted_map(self, list_of_chefs):
		get_tuple = lambda chef: w_chef(chef.since, chef)
		weights_s = list(map(get_tuple, list_of_chefs))
		weights_s.sort(reverse=True, key=lambda tup: tup.since)
		for w_c in weights_s:
			pass
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

	def _print_chef_stats(self, day):
		stats = self._day_of_week(day) + "\n"
		for chef in self.chefs_main:
			stats += str(chef) + "    since: " + str(chef.since) + ", times: " + str(chef.times) + "\n"
		print(stats)

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

	def _is_fair(self):
		main_dist = {}
		side_dist = {}
		week = -1
		week_main = []
		week_side = []
		for (index, (main, side)) in enumerate(self.schedule):
			main_dist[main] = 1 if main not in main_dist else main_dist[main] + 1
			side_dist[side] = 1 if side not in side_dist else side_dist[side] + 1

			if index % Chef.days_in_week == 0:
				week += 1
				week_main.append({})
				week_side.append({})

			week_main[week][main] = 1 if main not in week_main[week] else week_main[week] + 1
			week_side[week][side] = 1 if side not in week_side[week] else week_side[week] + 1


		main_unfairness = 0 # unfairness rises when conditions are not met
		side_unfairness = 0

		for key in main_dist:
			if main_dist[key] != 2:
				main_unfairness += 1
				print(key.name + "'s schedule is not fair. They cook a main " + str(main_dist[key]) + " times.")

		for key in side_dist:
			if side_dist[key] != 2: 
				side_unfairness += 1
				print(key.name + "'s schedule is not fair. They cook a side " + str(side_dist[key]) + " times.")

		for i in range(week):
			for key in week_main[i]:
				if week_main[i][key] > 1:
					main_unfairness += 1
					print(key.name + "'s schedule is not fair. They cook a main " + str(week_main[i][key]) + " times in a week.")
			for key in week_side[i]:
				if week_side[i][key] > 1:
					side_unfairness += 1
					print(key.name + "'s schedule is not fair. They cook a side " + str(week_side[i][key]) + " times in a week.")



		return (main_unfairness, side_unfairness)



