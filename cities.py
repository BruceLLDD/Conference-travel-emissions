from typing import Dict, List, Tuple
import math



class City:
    def __init__(self, name: str, country: str, citizens: int,
                 latitude: float, longitude: float):
        self.name = name
        self.country = country
        self.citizens = citizens
        self.latitude = latitude
        self.longitude = longitude
        if (type(self.name) != type('str')):
            raise Exception('name should be passed as strings')
        if (type(self.country) != type('str')):
            raise Exception('country should be passed as strings')
        if (self.citizens < 0):
            raise Exception('attendees must be a positive number')
        if (self.latitude < -90 or self.latitude > 90):
            raise Exception('latitude should be restricted to the -90 to 90')
        if (self.longitude < -180 or self.longitude > 180):
            raise Exception('longitude should be restricted to the -180 to 180')

    # calculate the distance  from a city to another
    def distance_to(self, other: 'City') -> float:
        Buenos_Aires = 'City'
        lati1 = self.latitude
        lati2 = other.latitude
        long1 = self.longitude
        long2 = other.latitude
        R = 6371
        distance = 2 * R * math.asin(math.sqrt(math.pow(math.sin((lati2 - lati1) / 2), 2) +
                                               math.cos(lati1) * math.cos(lati2) *
                                               math.pow(math.sin((long2 - long1) / 2), 2)))
        return distance

    def co2_to(self, other: 'City') -> float:
        self.distance_to(Buenos_Aires)


class CityCollection:


    def __init__(self, list_cities: list, country: list, total_attendees: int):
        self.cities = list_cities
        self.countries = country
        self.total_attendees = total_attendees

    def countries(self) -> List[str]:
        return self.countries()

    def total_attendees(self) -> int:
        return self.total_attendees()

    def total_distance_travel_to(self, city: City) -> float:
        raise NotImplementedError

    def travel_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def total_co2(self, city: City) -> float:
        raise NotImplementedError

    def co2_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def summary(self, city: City):
        raise NotImplementedError

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        raise NotImplementedError

    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError


# list_of_cities = ['zurich', 'san_francisco']
# city_collection =CityCollection(list_of_cities)
# print(city_collection.cities == list_of_cities)






Algiers = City('Algiers', 'Algeria', 1, 28.0000272, 2.9999825)

Buenos_Aires = City('Buenos_Aires', 'Argentina', 5, -34.6075616, -58.437076)


print(Algiers.distance_to(Buenos_Aires))