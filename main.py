from chef import Chef, Const
from scheduler import Scheduler

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


def main():
	scheduler = Scheduler(start_day=Const.MON)
	add_the_squad(scheduler)
	scheduler.schedule_three_weeks()
	scheduler.print_schedule()
	scheduler.print_fairness()


if __name__ == '__main__':
	main()