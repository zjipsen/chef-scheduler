from chef import Chef, Const
from scheduler import Scheduler

def add_the_squad(scheduler):
	main_chefs = [
	Chef("Alex", unavailable=[Const.MON, Const.TUES]),
	Chef("Maddy", unavailable=[Const.MON, Const.TUES]),
	Chef("Austin", unavailable=[Const.MON], since=4),
	Chef("John", unavailable=[Const.TUES]),
	Chef("Zana", since=1),
	Chef("Steph", since=2),
	Chef("Adam")
	]

	for chef in main_chefs:
		scheduler.add_chef(chef)

	side_chefs = [
	Chef("Alex", unavailable=[Const.MON, Const.TUES], since=4),
	Chef("Maddy", unavailable=[Const.MON, Const.TUES]),
	Chef("Austin", unavailable=[Const.MON]),
	Chef("John", unavailable=[Const.TUES]),
	Chef("Zana"),
	Chef("Adam"),
	Chef("Steph")
	]

	for chef in side_chefs:
		scheduler.add_chef(chef, False)

def main():
	scheduler = Scheduler(start_day=Const.MON)
	add_the_squad(scheduler)
	scheduler.schedule_three_weeks()
	scheduler.print_schedule()
	scheduler.print_fairness()


if __name__ == '__main__':
	main()