from chef import Chef, Const
from scheduler import Scheduler

def add_the_squad(scheduler):
	scheduler.add_chef(Chef("John", [Const.TUES]))
	scheduler.add_chef(Chef("Austin", [Const.MON]))
	scheduler.add_chef(Chef("Steph"))
	scheduler.add_chef(Chef("Zana", [Const.WED]))
	scheduler.add_chef(Chef("Alex", [Const.MON, Const.TUES]))
	scheduler.add_chef(Chef("Adam"))
	scheduler.add_chef(Chef("Maddy", [Const.MON, Const.TUES]))

	scheduler.add_chef(Chef("Austin", [Const.MON]), False)
	scheduler.add_chef(Chef("Alex", [Const.MON]), False)
	scheduler.add_chef(Chef("Zana", [Const.WED]), False)
	scheduler.add_chef(Chef("John", [Const.TUES]), False)
	scheduler.add_chef(Chef("Adam"), False)
	scheduler.add_chef(Chef("Steph"), False)
	scheduler.add_chef(Chef("Maddy", [Const.MON, Const.TUES]), False)

def main():
	scheduler = Scheduler()
	add_the_squad(scheduler)
	scheduler.schedule_three_weeks()
	scheduler.print_schedule()


if __name__ == '__main__':
	main()