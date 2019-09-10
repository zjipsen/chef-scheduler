from chef import Chef, Const
from scheduler import Scheduler
from messenger import Messenger
from datetime import datetime

def add_the_squad(scheduler):

	main_chefs = [
		Chef("Alex", unavailable=[Const.MON, Const.TUES]),
		Chef("Maddy", unavailable=[Const.MON, Const.TUES]),
		Chef("Austin", unavailable=[Const.MON]),
		Chef("John", unavailable=[Const.TUES]),
		Chef("Zana", unavailable=[Const.WED]),
		Chef("Steph"),
		Chef("Adam")
	]

	side_chefs = [
		Chef("Maddy", unavailable=[Const.MON, Const.TUES]),
		Chef("Alex", unavailable=[Const.MON]),
		Chef("Austin", unavailable=[Const.MON]),
		Chef("John", unavailable=[Const.TUES]),
		Chef("Zana", unavailable=[Const.WED]),
		Chef("Adam"),
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
	19494392557
]

def main():
	scheduler = Scheduler(start_day=Const.TUES, start_date=datetime.date(datetime(2019, 9, 10)), num_days=7)
	add_the_squad(scheduler)
	scheduler.find_fair()

	messenger = Messenger()
	print(scheduler.string_schedule())
	# messenger.send_message(scheduler.string_schedule(3), numbers[0])

if __name__ == '__main__':
	main()




