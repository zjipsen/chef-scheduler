from chef import Chef
from filter import Filter
import random
from datetime import timedelta
import math
from collections import namedtuple

class w_chef:
	def __init__(self, weight, chef):
		self.weight = weight
		self.chef = chef

class Scheduler:

	def __init__(self, start_day=0, start_date=None, num_days=14):
		self.num_days = num_days
		self.start_day = start_day
		self.start_date = start_date
		
		self.chefs_main = []
		self.chefs_side = []
		self.schedule = [None] * self.num_days
		self.roommates = {}
		self.max_times_per_period = 2
		self.nobody = Chef("**Nobody**")


	# Public Methods ####################################################################
	def add_roommate_config(self, roommates):
		self.roommates = roommates

	def add_chef(self, chef, main=True):
		if (main):
			self.chefs_main.append(chef)
		else:
			self.chefs_side.append(chef)

		self.max_times_per_period = math.ceil(self.num_days / float(len(self.chefs_main)))

	def find_fair(self):
		for i in range(100):
			self._reset()
			random.shuffle(self.chefs_main)
			random.shuffle(self.chefs_side)
			self.schedule_three_weeks()

			fairness = self._is_fair(do_print=False)
			# if fairness[0] == 0:
			# 	print("Main chef entry order results in fair schedule.\n" + str([chef.name for chef in self.chefs_main]) + "\n")
			# if fairness[1] == 0:
			# 	print("Side chef entry order results in fair schedule.\n" + str([chef.name for chef in self.chefs_side]) + "\n")
			if fairness[0] == 0 and fairness[1] == 0:
				# self.print_schedule()
				print("\nSucceeded after " + str(i + 1) + " attempts.\n")
				return True
	

	def schedule_three_weeks(self):
		for day, sched in enumerate(self.schedule):
			self._schedule_day(day)

	def print_schedule(self):
		print(self.string_schedule())

	def string_schedule(self):
		string = "Day:    Main   |  Side\n_____________________\n"
		date = self.start_date

		if date is not None:
			string += str(date.month) + "-" + str(date.day) +  "\n"
			date = date + timedelta(days=1)

		for i, schedule in enumerate(self.schedule):
			actual_day = i + self.start_day

			if (schedule):
				string += (self._day_of_week(actual_day) + str(schedule[0]) + "|" + str(schedule[1])) + "\n"
			else:
				string += (self._day_of_week(actual_day) + "Nobody cooks") + "\n"
			if (actual_day % Chef.days_in_week == Chef.days_in_week - 1):
				string += "\n"
				if date is not None:
					date = date + timedelta(days=2)
					string += str(date.month) + "-" + str(date.day) +  "\n"

			if date is not None:
				date = date + timedelta(days=1)
		return string

	def print_fairness(self):
		(main_unfair, side_unfair) = self._is_fair()
		print("_________________________________")
		print("Main unfairness: " + str(main_unfair))
		print("Side unfairness: " + str(side_unfair))
		print("")

	# Private Methods ###################################################################

	"""
	Schedule one day given the chefs, their availability and cooking record, and what day it is today.
	day: int < 14
	"""
	def _reset(self):
		self.schedule = [None] * self.num_days

		for chef in self.chefs_main:
			chef.since = chef.init_since
			chef.times = 0

		for chef in self.chefs_side:
			chef.since = chef.init_since
			chef.times = 0

	def _schedule_day(self, day):
		actual_day = day + self.start_day
		index = day

		(main, side) = self._choose(actual_day)
		self.schedule[index] = (main, side)

		for chef in self.chefs_main:
			if main:
				if (chef.name == main.name):
					chef.cook()
				else:
					chef.dont_cook()

		for chef in self.chefs_side:
			if side:
				if (chef.name == side.name):
					chef.cook()
				else:
					chef.dont_cook()
		#self._print_chef_stats(actual_day)

	def _get_sorted_map(self, list_of_chefs):
		weights = [w_chef(chef.since, chef) for chef in list_of_chefs]
		weights.sort(reverse=True, key=lambda wc: wc.weight)
		return weights

	def _find_available_chef(self, sorted_chefs, day):
		current_day = day % Chef.days_in_week
		available = []
		for (index, sorted_chef) in enumerate(sorted_chefs):
			chef = sorted_chef.chef
			if current_day not in chef.unavailable and chef.times < self.max_times_per_period:
				available.append(sorted_chef)
		if len(available) > 0 and available[0].weight == -1:
			print("well, this would have rather been avoided")
		return available[0].chef if len(available) > 0 else None

	def _yesterdays_chefs(self, day):
		if (day > self.start_day):
			yesterday = day - self.start_day - 1
			if self.schedule[yesterday] is not None:
				(main, side) = self.schedule[yesterday]
				return [main.name, side.name]
		return []

	def _get_sorted_map_main(self, yesterdays_chefs=[]):
		filt = Filter()

		weights_m = self._get_sorted_map(self.chefs_main)
		weights_m = filt.yesterday(yesterdays_chefs, weights_m)
		return weights_m

	def _get_sorted_map_side(self, main, yesterdays_chefs):
		filt = Filter()

		weights_s = self._get_sorted_map(self.chefs_side)
		weights_s = filt.yesterday(yesterdays_chefs, weights_s)
		weights_s = filt.same_person(main, weights_s)
		weights_s = filt.roommates(main, self.roommates, weights_s)
		return weights_s

	def _choose(self, day):
		yesterdays_chefs = self._yesterdays_chefs(day)

		# choose main chef
		weights_m = self._get_sorted_map_main(yesterdays_chefs)
		main = self._find_available_chef(weights_m, day)

		# choose side chef
		weights_s = self._get_sorted_map_side(main, yesterdays_chefs)
		side = self._find_available_chef(weights_s, day)

		if main is None:
			main = self.nobody
		if side is None:
			side = self.nobody

		return (main, side)

	def _print_chef_stats(self, day):
		stats = self._day_of_week(day) + "\n"
		for chef in self.chefs_side:
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

	def _get_empty_dict(self):
		return {
			"Alex": 0,
			"Zana": 0,
			"Adam": 0,
			"John": 0,
			"Maddy": 0,
			"Steph": 0,
			"Austin": 0
		}

	def _is_fair(self, do_print=True):
		main_dist = self._get_empty_dict()
		side_dist = self._get_empty_dict()
		week = -1
		week_main = []
		week_side = []
		for (index, (main, side)) in enumerate(self.schedule):
			if main != self.nobody:
				main_dist[main.name] += 1
			if side != self.nobody:
				side_dist[side.name] += 1

				if index % Chef.days_in_week == 0:
					week += 1
					week_main.append(self._get_empty_dict())
					week_side.append(self._get_empty_dict())
			if main != self.nobody:
				week_main[week][main.name] += 1
			if side != self.nobody:
				week_side[week][side.name] += 1


		main_unfairness = 0 # unfairness rises when conditions are not met
		side_unfairness = 0

		for key in main_dist:
			if main_dist[key] != self.max_times_per_period:
				main_unfairness += 1
				if do_print:
					print(key + "'s schedule is not fair. They cook a main " + str(main_dist[key]) + " times.")

		for key in side_dist:
			if side_dist[key] != self.max_times_per_period:
				side_unfairness += 1
				if do_print:
					print(key + "'s schedule is not fair. They cook a side " + str(side_dist[key]) + " times.")

		for i in range(week):
			for key in week_main[i]:
				if week_main[i][key] > 1:
					main_unfairness += 1
					if do_print:
						print(key + "'s schedule is not fair. They cook a main " + str(week_main[i][key]) + " times in a week.")
			for key in week_side[i]:
				if week_side[i][key] > 1:
					side_unfairness += 1
					if do_print:
						print(key + "'s schedule is not fair. They cook a side " + str(week_side[i][key]) + " times in a week.")

		return (main_unfairness, side_unfairness)



