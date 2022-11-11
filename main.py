from utils import collection
from cities import City, CityCollection
if __name__ == '__main__':
    print(collection[1])
    Algiers = City('Algiers', 'Algeria', 1, 28.0000272, 2.9999825)

    Buenos_Aires = City('Buenos_Aires', 'Argentina', 5, -34.6075616, -58.437076)

    print(Algiers.distance_to(Buenos_Aires))

    Algiers.co2_to(Buenos_Aires)
    list_of_cities = ['zurich', 'san_francisco']
    city_collection = CityCollection(list_of_cities)
    print(city_collection.cities == list_of_cities)
