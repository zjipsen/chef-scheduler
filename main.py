from chef import Chef, Const
from scheduler import Scheduler

def add_the_squad(scheduler):
	main_chefs = [
	Chef("Alex", [Const.MON, Const.TUES]),
	Chef("Maddy", [Const.MON, Const.TUES]),
	Chef("Austin", [Const.MON]),
	Chef("John", [Const.TUES]),
	Chef("Zana", [Const.WED]),
	Chef("Steph"),
	Chef("Adam")
	]

	for chef in main_chefs:
		scheduler.add_chef(chef)

	side_chefs = [
	Chef("Alex", [Const.MON, Const.TUES]),
	Chef("Maddy", [Const.MON, Const.TUES]),
	Chef("Austin", [Const.MON]),
	Chef("John", [Const.TUES]),
	Chef("Zana", [Const.WED]),
	Chef("Adam"),
	Chef("Steph")
	]

	for chef in side_chefs:
		scheduler.add_chef(chef, False)


def main():
	scheduler = Scheduler()
	add_the_squad(scheduler)
	scheduler.schedule_three_weeks()
	scheduler.print_schedule()
	scheduler.print_fairness()


if __name__ == '__main__':
	main()