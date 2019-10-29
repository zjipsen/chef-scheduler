from enum import Enum, unique
@unique
class DAYS(Enum):
    SUN = 0
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    DAYS = [SUN, MON, TUE, WED, THU]
