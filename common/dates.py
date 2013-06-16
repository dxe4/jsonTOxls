import datetime
import random

#TODO fix random days
def random_date(year=None, month=None, day=None):
    """
        Creates a random date.
        WARNING: random days = 1-28 (29-31 wont get generated for now)
    :param year: if value passed wont be random
    :param month: if value passed wont be random
    :param day: if value passed wont be random
    """
    month = month if month else random.randrange(1, 12)
    day = day if day else random.randrange(1, 28)
    year = year if year else random.randrange(2013, 2014)
    print(year, month, day)
    return datetime.date(year, month, day)

#TODO fix random days
def random_dates_sorted(year=None, month=None, day=None):
    """
        Creates a 2 random dates, and returns them sorted.
        WARNING: random days = 1-28 (29-31 wont get generated for now)
    :param year: if value passed wont be random
    :param month: if value passed wont be random
    :param day: if value passed wont be random
    :return: date_1 date_2 where date1 is before date_2
    """
    date_1 = random_date(year=year, month=month, day=day)
    date_2 = random_date(year=year, month=month, day=day)
    if date_1 if date_1 < date_2 else date_2:
        return date_1, date_2
    else:
        return date_2, date_1


