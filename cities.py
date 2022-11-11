from typing import Dict, List, Tuple
import math
import matplotlib.pyplot as plt


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
        lati1 = self.latitude
        lati2 = other.latitude
        long1 = self.longitude
        long2 = other.longitude
        R = 6371
        distance = 2 * R * math.asin(math.sqrt(math.pow(math.sin((lati2 - lati1) / 2), 2) +
                                               math.cos(lati1) * math.cos(lati2) *
                                               math.pow(math.sin((long2 - long1) / 2), 2)))
        return distance

    def co2_to(self, other: 'City') -> float:
        distance = self.distance_to(other)
        if (distance >= 0 and distance <= 1000):
            emit = self.citizens * 200 * distance
        elif (distance > 1000 and distance <= 8000):
            emit = self.citizens * 250 * distance
        else:
            emit = self.citizens * 300 * distance
        return emit


class CityCollection:

    def __init__(self, list_cities: list):
        self.cities = list_cities

    def countries(self) -> List[str]:
        countries_list = []
        for i in self.cities:
            if i.country not in countries_list:
                countries_list.append(i.country)

        return countries_list

    def total_attendees(self) -> int:
        attendees = 0
        for i in self.cities:
            new_attendees = i.citizens
            attendees = attendees+new_attendees
        return attendees

    def total_distance_travel_to(self, city: City) -> float:
        total_distance = 0.
        for i in self.cities:
            distance = i.distance_to(city)*i.citizens
            total_distance = total_distance+distance
        return total_distance

    def travel_by_country(self, city: City) -> Dict[str, float]:
        countries = self.countries()
        dict_distance = {}.fromkeys(countries, 0.)
        for i in self.cities:
            country = i.country
            distance = i.citizens*i.distance_to(city)
            dict_distance[country] += distance
        return dict_distance


    def total_co2(self, city: City) -> float:
        total_co2 = 0.
        for i in self.cities:
            co2 = i.co2_to(city) * i.citizens
            total_co2 = total_co2 + co2
        return total_co2

    def co2_by_country(self, city: City) -> Dict[str, float]:
        countries = self.countries()
        dict_co2 = {}.fromkeys(countries, 0.)
        for i in self.cities:
            country = i.country
            co2 = i.citizens * i.co2_to(city)
            dict_co2[country] += co2
        return dict_co2

    def summary(self, city: City):
        print(f'Host city: {city.name} ({city.country})')
        print(f'Total CO2: {round(self.total_co2(city)/1000)} tonnes')
        print(f'Total attendees travelling to {city.name} from {len(self.cities)-1} different cities: {self.total_attendees()-city.citizens}')


    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        list0 = []
        for i in self.cities:
            total_co2 = self.total_co2(i)
            list0.append((i.name, total_co2))
        result = sorted(list0, key=lambda x: (x[1], x[0]))
        return result




    def plot_top_emitters(self, city: City, n: int, save: bool):
        dict_countries = self.co2_by_country(city)
        sorted_countries = sorted(dict_countries.items(), key=lambda dc: (dc[1], dc[0]), reverse=True)

        countries = []
        total_emissions = []
        other_emissions = 0.
        for i in range(n):
            countries.append(sorted_countries[i][0])
            total_emissions.append(sorted_countries[i][1]/1000)
        for i in range(n, len(sorted_countries)):
            other_emissions = other_emissions + sorted_countries[i][1]

        countries.append('Everywhere else')
        total_emissions.append(other_emissions/1000)
        plt.figure(figsize=(15, 15))
        plt.xticks(rotation=45, fontsize=14)
        plt.bar(countries, total_emissions, color=['r', 'g', 'b'])
        plt.title(f"Total emissions from each country(top {n})")
        plt.ylabel("Total emissions (tonnes CO2)")
        if save:
            plt.savefig("./buenos_aires.png")
        else:
            plt.show()

