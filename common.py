import random
import datetime

a_to_z = range(ord("a"), ord("z"))


def number_to_cell(row, col):
    new_row = chr(a_to_z[col]).upper()
    return new_row.upper() + str(row)


def number_to_cell(col):
    return chr(a_to_z[col]).upper()


def number_to_cells(columns):
    return [chr(a_to_z[col]).upper() for col in columns]


def random_list_item(list):
    index = random.randrange(0, list.__len__())
    return list[index]

get_dict = lambda dictionary, key: dictionary[key] if key in dictionary else None;
pop_dict = lambda dictionary, key: dictionary.pop(key) if key in dictionary else {};

def safe_get_dict(dictionary, key, method):
    functions = {
        "pop":pop_dict,
        "get": get_dict
    }
    f = functions[method]
    return f(dictionary, key)


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