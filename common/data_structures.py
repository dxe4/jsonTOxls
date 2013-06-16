import random


def random_list_item(list):
    """
        Selects a random item from the given list
    :param list: list to select from
    :return: random item from list
    """
    index = random.randrange(0, list.__len__())
    return list[index]