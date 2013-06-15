from random import randrange
from datetime import timedelta, time
import datetime
import random
from common import data_structures, dates


class Example4:
    def __init__(self, locations):
        self.locations = locations

    def random_days_dict(self):
        date_list = {}
        departure_list = []
        arrival_list = []
        for i in range(1, 10):
            departure_date, arrival_date = dates.random_dates_sorted(year=2013)
            departure_list.append(departure_date)
            arrival_list.append(arrival_date)
        date_list["Departure"] = departure_list
        date_list["Arrival"] = arrival_list
        return date_list

    def random_companies(self, dates):
        companies = {}
        for i in range(2, 8):
            company_key = "company " + str(random.randrange(1, 10))
            companies[company_key] = self.random_prices(dates)
        return companies

    def random_price(self):
        if random.randrange(1, 4) > 1:
            return "%.2f" % random.uniform(50.00, 499.99)
        else:
            return None

    def random_prices(self, dates):
        price_map = {}
        for k, v in dates.items():
            for date in v:
                price_map[date] = self.random_price()
        return price_map

    def create_data(self):
        data = {}
        for i in range(1, 10):
            departure_location, arrival_location = \
                data_structures.random_list_item(self.locations), data_structures.random_list_item(self.locations)
            dates = self.random_days_dict()
            companies = self.random_companies(dates)
            data[i] = {"Departure": departure_location, "Arrival": arrival_location,
                       "dates": dates, "companies": companies}
        return data


