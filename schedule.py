from chef import Chef, NOBODY

class Day:

    def __init__(self, date, day_of_week, main=NOBODY, side=NOBODY, vacation=[]):
    self.date = date
    self.day_of_week = day_of_week
    self.main = main
    self.side = side
    self.which_week = self.get_which_week(date)
    self.vacation = vacation

    # Static Methods #####################################################
    
    def get_which_week(self, date):
        # Returns a datetime object: the Sunday at the beginning of the week that includes *date*.
        pass


class Schedule:
    """
    Data structure: schedule is a list of Days, always in increasing order of the Day.date (a python datetime object).
    """

    def __init__(self):
        self.schedule = []

    def find_day(self, date):
        pass

    def get_fairness(self):
        pass
    
    def get_weeks(self, date=None):
        # returns an iterable of lists of Days with a max length of 7. Breaks the schedule up into weeks.
        # If date is not null, start with that date and continue forward from there.
        pass

    def jsonify(self):
        pass

    def set_days(self, days=[]):
        pass

    def test_fairness(self, days=[]):
        pass

    def stringify(self, date=None):
        if date is None:
            date = self.schedule[0].date

        string = "Day:    Main   |  Side\n_____________________\n"
        for week in self.get_weeks(date):
            string += str(week[0].which_week.month) + "-" + str(week[0].which_week.day) +  "\n"
            for day in week:
                string += day.day_of_week + ": " + day.main + "|" + day.side + "\n"
            string += "\n"
        
        return string

    # Private Methods ####################################################

    def _set_day(self):
        for day in self.schedule:
            pass



