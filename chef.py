class Const:
    SUN = 0
    MON = 1
    TUES = 2
    WED = 3
    THURS = 4
    DAYS = [SUN, MON, TUES, WED, THURS]

class Chef: 
    days_in_week = 5

    def __init__(self, name, unavailable=[], since=6, times=0):
        self.name = name
        self.unavailable = unavailable
        self.since = since
        self.times = times
        self.init_since = since

    def cook(self):
        self.since = max(self.since - 6, 0)
        self.times += 1
        # if (self.times == 2):
        #     self.make_unavailable_from(day)

    def make_unavailable_from(self, day):
        pass
        # while (day < len(self.unavailable)):
        #     self.unavailable[day] = 0
        #     day = day + 1

    def dont_cook(self):
        self.since += 1

    """
    def swap_nights(self, otherChef):
        pass

    def add_week(self, week):
        pass
    """

    def __str__(self):
        return " " + self.name + self.padding_to_six()

    def padding_to_six(self):
        return " " * (6 - len(self.name) + 1)


        