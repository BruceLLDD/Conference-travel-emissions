from cities import City, CityCollection
from pathlib import Path
import csv


file_path = Path("attendee_locations.csv")


def read_attendees_file(file_path) -> CityCollection:
    # return file_path.read_text()
    city_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)     # delete the first row
        for row in reader:
            city = City(row[3], row[1], int(row[0]), float(row[4]), float(row[5]))
            city_list.append(city)
        city_collection = CityCollection(city_list)

    return city_collection


collection = read_attendees_file(file_path)  # type(collection) is list

# list_of_cities = []
# for i in collection:
#     city = i[-4]
#     list_of_cities.append(city)
# del(list_of_cities[0])

