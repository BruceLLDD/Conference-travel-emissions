import pytest
from cities import City, CityCollection
from pathlib import Path


# negative tests

#   test the name of city, which should be passed as strings
def test_city_name():
    with pytest.raises(ValueError) as exception:
        city = City(111, 'Argentina', 5, -34.6075616, -58.437076)
        assert "The name of city should be passed as strings" in str(exception.value)


#    test the number of attendees, which should be passed as a positive number
def test_city_citizens():
    with pytest.raises(ValueError) as exception:
        city = City('Algiers', 'Argentina', -1, -34.6075616, -58.437076)
        assert "The number of attendees should be passed as an integer and a positive number" in str(exception.value)


#    test the latitude, which should be restricted to the -90 to 90
def test_city_latitude():
    with pytest.raises(ValueError) as exception:
        city1 = City('Algiers', 'Argentina', 5, -91, -58.437076)
        city2 = City('Algiers', 'Argentina', 5, 91, -58.437076)
        assert "The latitude and longitude should be restricted to the -90 to 90" in str(exception.value)


#    test the longitude, which should be restricted to the -180 to 180
def test_city_longitude():
    with pytest.raises(ValueError) as exception:
        city1 = City('Algiers', 'Argentina', 5, -34.6075616, -181)
        city2 = City('Algiers', 'Argentina', 5, -34.6075616, 181)
        assert "The longitude should be restricted to the -180 to 180" in str(exception.value)


# test given city class methods

# test distance_to
def test_distance_to():
    pass


# test co2_to
def test_co2_to():
    pass
