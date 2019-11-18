class Chef: 
    days_in_week = 5

    def __init__(self, name, unavailable=[], since=6, times=0, vacation=False):
        self.name = name
        self.unavailable = unavailable
        self.since = since
        self.times = times
        self.init_since = since
        self.init_times = times
        self.vacation = vacation

    def cook(self):
        self.since = max(self.since - 6, 0)
        self.times += 1

    def dont_cook(self):
        self.since += 1

    def __str__(self):
        return " " + self.name + self.padding_to_six()

    def padding_to_six(self):
        return " " * (6 - len(self.name) + 1)
        
NOBODY = Chef("-")