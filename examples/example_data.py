import random
import common

class Example4Data:
    def __init__(self, locations):
        self.locations = locations

    def create_data(self):
        data = {}
        for i in range(1, 10):
            departure_location = common.random_list_item(self.locations)
            arrival_location = common.random_list_item(self.locations)
            dates = self.random_dates_dict()
            companies = self.random_companies(dates)
            data[i] = {
                "Departure": departure_location,
                "Arrival": arrival_location,
                "dates": dates,
                "companies": companies
            }
        return data

    def random_dates_dict(self):
        date_dict, departure_list, arrival_list = {}, [], []
        lambda_add = lambda list1, list2, arg1, arg2: (list1.append(arg1), list2.append(arg2))
        for i in range(1, 10):
            lambda_add(departure_list, arrival_list, *common.random_dates_sorted(year=2013))
        date_dict["Departure"], date_dict["Arrival"] = departure_list, arrival_list
        return date_dict

    def random_companies(self, dates):
        companies = {}
        for i in range(2, 8):
            company_key = "company " + str(random.randrange(1, 10))
            companies[company_key] = self.random_prices(dates)
        return companies

    def random_prices(self, dates):
        price_map = {}
        for description, dates in dates.items():
            price_list = []
            price_map[description] = price_list
            for date in dates:
                price_list.append({date: self.random_price()})
        return price_map

    def random_price(self, min=50.00, max=499.99):
        if random.randrange(1, 4) > 1:
            return "%.2f" % random.uniform(min, max)
        else:
            return None




