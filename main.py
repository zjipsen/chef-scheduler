from chef import Chef, Const
from scheduler import Scheduler
from messenger import Messenger
from datetime import datetime

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
	19494392557,
	12623431639
]

def main():
	scheduler = Scheduler(start_day=Const.SUN, start_date=datetime.date(datetime(2019, 9, 15)), num_days=10)
	add_the_squad(scheduler)
	scheduler.find_fair()

	messenger = Messenger()
	print(scheduler.string_schedule())
	# for number in numbers:
	# 	messenger.send_message(scheduler.string_schedule(), number)

if __name__ == '__main__':
	main()




