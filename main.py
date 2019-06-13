from chef import Chef
from scheduler import Scheduler

def add_the_squad(scheduler):
	scheduler.add_chef(Chef("John"))
	scheduler.add_chef(Chef("Austin"))
	scheduler.add_chef(Chef("Steph"))
	scheduler.add_chef(Chef("Zana"))
	scheduler.add_chef(Chef("Alex"))
	scheduler.add_chef(Chef("Adam"))

	scheduler.add_chef(Chef("Austin"), False)
	scheduler.add_chef(Chef("Alex"), False)
	scheduler.add_chef(Chef("Zana"), False)
	scheduler.add_chef(Chef("John"), False)
	scheduler.add_chef(Chef("Adam"), False)
	scheduler.add_chef(Chef("Steph"), False)

def main():
	scheduler = Scheduler()
	add_the_squad(scheduler)
	scheduler.schedule_fortnight()
	scheduler.print_schedule()


if __name__ == '__main__':
	main()