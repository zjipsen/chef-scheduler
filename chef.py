class Chef: 
    days_in_week = 5

    def __init__(self, name, schedule=[1]*days_in_week):
        self.name = name
        self.schedule = schedule
        self.since = 0
        self.times = 0

    def cook(self, day):
        self.since = 0
        self.times += 1
        if (self.times == 2):
            self.make_unavailable_from(day)

    def make_unavailable_from(self, day):
        while (day < len(self.schedule)):
            self.schedule[day] = 0
            day = day + 1

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