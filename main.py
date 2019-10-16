# -*- coding: utf-8 -*-
from chef import Chef
from scheduler import Scheduler
from messenger import Messenger
from datetime import datetime
from time import sleep
from daysOfTheWeek import DAYS_OF_THE_WEEK

def add_the_squad(scheduler):

	main_chefs = [
		Chef("Alex", unavailable=[DAYS_OF_THE_WEEK.MON.value, DAYS_OF_THE_WEEK.THU.value]),
		Chef("Maddy", unavailable=[DAYS_OF_THE_WEEK.MON.value, DAYS_OF_THE_WEEK.TUE.value, DAYS_OF_THE_WEEK.THU.value]),
		Chef("Austin", unavailable=[DAYS_OF_THE_WEEK.MON.value]),
		Chef("John", unavailable=[DAYS_OF_THE_WEEK.TUE.value]),
		Chef("Zana", unavailable=[DAYS_OF_THE_WEEK.WED.value, DAYS_OF_THE_WEEK.THU.value]),
		Chef("Adam", unavailable=[DAYS_OF_THE_WEEK.WED.value]),
		Chef("Steph"),
	]

	side_chefs = [
		# Chef("Maddy", unavailable=[DAYS_OF_THE_WEEK.MON.value, DAYS_OF_THE_WEEK.TUE.value]),
		Chef("Alex", unavailable=[DAYS_OF_THE_WEEK.MON.value, DAYS_OF_THE_WEEK.THU.value]),
		Chef("Austin", unavailable=[DAYS_OF_THE_WEEK.MON.value]),
		Chef("John", unavailable=[DAYS_OF_THE_WEEK.TUE.value]),
		Chef("Zana", unavailable=[DAYS_OF_THE_WEEK.WED.value, DAYS_OF_THE_WEEK.THU.value]),
		# Chef("Adam"),
		Chef("Steph")
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
	# ("Alexander", 12623431639),
	# ("Stephanie", 12623059455),
	# ("Maddy", 14143347626),
	# ("Austin", 18054045067),
	# ("John", 16084214427),
	# ("Adam", 12624429397)
]


potential = """
Day:    Main   |  Side
_____________________
9-29
Sun:  Steph  | -
Mon:  Zana   | -
Tue:  Adam   | Austin		off this week: Austin, Maddy
Wed:  Alex   | -
Thu:  John   | Steph

10-6
Sun:  Maddy  | Steph
Mon:  Adam   | Zana
Tue:  Austin | Alex 		off this week: Zana, Steph
Wed:  John   | -
Thu:  Alex   | John

10-13
Sun:  Zana   | Austin
Mon:  Steph  | -
Tue:  Adam   | Zana			off this week: Alex, Austin
Wed:  Maddy  | -
Thu:  John   | Steph

10-20
Sun:  Zana   | Austin
Mon:  Steph  | John			
Tue:  Alex   | -			off this week: 
Wed:  Austin | -
"""

manual_schedule = """
Here's next week's schedule!

Day:    Main   |  Side
_____________________
10-13
Sun:  Zana    | Austin
Mon:  Steph  | -
Tue:  Adam    | Zana
Wed:  Maddy | -
Thu:  John     | Steph
"""


def main():
	scheduler = Scheduler(start_day= DAYS_OF_THE_WEEK.TUE.value, start_date=datetime.date(datetime(2019, 10, 15)), num_days=7)
	add_the_squad(scheduler)
	scheduler.find_fair()

	messenger = Messenger()
	print(scheduler.string_schedule())
	print(scheduler.json_schedule())
	
	schedule = manual_schedule

	""" 
		ALWAYS send to myself first before sending out, to check formatting and validity. 
		DON'T FORGET TO UPDATE SHARED NOTE.
	"""
	for (name, number) in numbers:
		sleep(1)
		messenger.send_message(schedule, number)
		
		pass		
		# messenger.send_message('\\(*^ _ ^*)/ \nHello ' + name + ', I am the scheduling bot! Please save my number! Here is the schedule for next week:', number)

if __name__ == '__main__':
		main()




