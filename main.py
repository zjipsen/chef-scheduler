# -*- coding: utf-8 -*-
from chef import Chef, Const
from scheduler import Scheduler
from messenger import Messenger
from datetime import datetime
from time import sleep

def add_the_squad(scheduler):

	main_chefs = [
		Chef("Alex", unavailable=[Const.MON, Const.TUES]),
		Chef("Maddy", unavailable=[Const.MON, Const.TUES]),
		# Chef("Austin", unavailable=[Const.MON]),
		Chef("John", unavailable=[Const.TUES]),
		Chef("Zana", unavailable=[Const.WED]),
		# Chef("Steph"),
		Chef("Adam")
	]

	side_chefs = [
		Chef("Maddy", unavailable=[Const.MON, Const.TUES]),
		Chef("Alex", unavailable=[Const.MON]),
		# Chef("Austin", unavailable=[Const.MON]),
		Chef("John", unavailable=[Const.TUES]),
		Chef("Zana", unavailable=[Const.WED]),
		Chef("Adam"),
		# Chef("Steph")
	]

	roommates = {
		"Alex": ["Zana"],
		"Zana": ["Alex"],
		"Adam": ["Maddy", "John"],
		"John": ["Adam", "Maddy"],
		"Maddy": ["Adam", "John"],
		"Steph": ["Austin"],
		"Austin": ["Steph"]
	}

	for chef in main_chefs:
		scheduler.add_chef(chef)

	for chef in side_chefs:
		scheduler.add_chef(chef, False)

	scheduler.add_roommate_config(roommates)

numbers = [
	("Zana", 19494392557),
	("Alexander", 12623431639),
	# ("Stephanie", 12623059455),
	("Maddy", 14143347626),
	# ("Austin", 18054045067),
	("John", 16084214427),
	("Adam", 12624429397)
]

manual_schedule = """
Day:    Main   |  Side
_____________________
9-15
Sun:  Adam   | Alex
Mon:  John   | Zana
Tue:  Zana   | Adam
Wed:  Maddy  | John
Thu:  Alex   | Maddy
"""


def main():
	scheduler = Scheduler(start_day=Const.SUN, start_date=datetime.date(datetime(2019, 9, 15)), num_days=5)
	add_the_squad(scheduler)
	scheduler.find_fair()

	messenger = Messenger()
	print(scheduler.string_schedule())
	
	schedule = manual_schedule

	for (name, number) in numbers:
		pass
		# sleep(1)
		# messenger.send_message(schedule, number)
		# messenger.send_message('\\(*^ _ ^*)/ \nHello ' + name + ', I am the scheduling bot! Please save my number! Here is the schedule for next week:', number)

if __name__ == '__main__':
	main()




