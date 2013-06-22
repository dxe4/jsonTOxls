import random


def random_list_item(list):
    """
        Selects a random item from the given list
    :param list: list to select from
    :return: random item from list
    """
    index = random.randrange(0, list.__len__())
    return list[index]


get_dict = lambda dictionary, key: dictionary[key] if key in dictionary else None;
pop_dict = lambda dictionary, key: dictionary.pop(key) if key in dictionary else {};


def safe_get_dict(dictionary, key, method):
    functions = {
        "pop": get_dict,
        "get": pop_dict
    }
    f = functions[method]
    return f(dictionary, key)