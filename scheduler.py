from chef import Chef
import random

class Scheduler:
	def __init__(self):
		self.chefs_main = []
		self.chefs_side = []
		self.schedule = [None]*14
		#self.last_week = []
		#self.day_buffer = 4
		#self.must_cook_days = 2
		#self.cancelled = [] # list of days no one should cook; 1 = Monday, 2 = Tuesday, ... 7 = Sunday

	def add_chef(self, chef, main=True):
		if (main):
			self.chefs_main.append(chef)
		else:
			self.chefs_side.append(chef)

	def schedule_fortnight(self):
		for day, sched in enumerate(self.schedule):
			self.schedule_day(day)

	"""
	Schedule one day given the chefs, their availability and cooking record, and what day it is today.
	day: int < 14
	"""
	def schedule_day(self, day):
		main = random.choice(self.chefs_main) # throwaway for now
		side = random.choice(self.chefs_side) # throwaway for now

		self.schedule[day] = (main, side)

		for chef in self.chefs_main:
			if (chef.name == main.name):
				chef.cook(day)
			else:
				chef.dont_cook()

		for chef in self.chefs_side:
			if (chef.name == side.name):
				chef.cook(day)
			else:
				chef.dont_cook()

	def day_of_week(self, day):
		day = (day + 1) % 7
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
		if (day == 5):
			name = "Fri"
		if (day == 6):
			name = "Sat"
		return name + ": "

	def print_schedule(self):
		print("\n      Main   | Side\n_____________")
		for i, day in enumerate(self.schedule):
			if (day):
				print(self.day_of_week(i) + str(day[0]) + "|" + str(day[1]))
			else:
				print(self.day_of_week(i) + "Nobody cooks")
			if (i == 6):
				print(" ")	
		print("\n")
	"""
	def next_week(self):
		pass
	"""



