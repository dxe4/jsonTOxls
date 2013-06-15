from random import randrange
from datetime import timedelta, time
import datetime
import random
from common import data_structures, dates


class Example4:
    def __init__(self, locations):
        self.locations = locations

    def create_data(self):
        data = {}
        for i in range(1, 10):
            departure_location, arrival_location = \
                data_structures.random_list_item(self.locations), data_structures.random_list_item(self.locations)
            dates = self.random_dates_dict()
            companies = self.random_companies(dates)
            data[i] = {"Departure": departure_location, "Arrival": arrival_location,
                       "dates": dates, "companies": companies}
        return data

    def random_dates_dict(self):
        """
        Create random dates
        :return: dates map Arrival:[date]
        """
        date_dict = {}
        departure_list = []
        arrival_list = []
        for i in range(1, 10):
            departure_date, arrival_date = dates.random_dates_sorted(year=2013)
            departure_list.append(departure_date)
            arrival_list.append(arrival_date)
        date_dict["Departure"] = departure_list
        date_dict["Arrival"] = arrival_list
        return date_dict

    def random_companies(self, dates):
        """
        Create random companies
        :param dates: dates dictionary, Arrival:[date]
        :return: map company:arrival{[date:price]}
        """
        companies = {}
        for i in range(2, 8):
            company_key = "company " + str(random.randrange(1, 10))
            companies[company_key] = self.random_prices(dates)
        return companies

    def random_prices(self, dates):
        """
        Creates a map from date to random price
        :param dates: dates dictionary -> Arrival:dates , Departure:dates
        :return: prices map -> arrival{[date:price]}
        """
        price_map = {}
        for description, dates in dates.items():
            price_list = []
            price_map[description] = price_list
            for date in dates:
                price_list.append({date:self.random_price()})
        return price_map

    def random_price(self,min = 50.00,max = 499.99):
        """
        Creates a random float used as a price with 2 decimal points
        :param min: default 50.00
        :param max: default 499.99
        :return: random float with 2 decimal points. default min,max : 50 499.99
        """
        if random.randrange(1, 4) > 1:
            return "%.2f" % random.uniform(min, max)
        else:
            return None



