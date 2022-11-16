import pytest
from cities import *
from utils import *
from pytest import *


@pytest.fixture()
def Algiers():
    Algiers = City('Algiers', 'Algeria', 1, 28.0000272, 2.9999825)
    return Algiers


@pytest.fixture()
def Buenos_Aires():
    Buenos_Aires = City('Buenos_Aires', 'Argentina', 5, -34.6075616, -58.437076)
    return Buenos_Aires


@pytest.fixture()
def Zurich():
    Zurich = City('Zurich', 'Switzerland', 109, 47.3723941, 8.5423328)
    return Zurich


@pytest.fixture()
def Canberra():
    Canberra = City('Australia', 'Canberra', 54, -35.2975906, 149.1012676)
    return Canberra


@pytest.fixture()
def Graz():
    Graz = City('Austria', 'Graz', 14, 47.0708678, 15.4382786)
    return Graz


@pytest.fixture()
def London():
    London = City('United Kingdom', 'London', 117, 51.5073219, -0.1276474)
    return London


#  test given city class methods

class TestCities:
    # test distance_to
    def test_distance_to(self, Zurich: City, London: City):
        expect_distance = Zurich.distance_to(London)
        real_distance = 776.05
        assert abs(expect_distance - real_distance) < 50

    # test co2_to
    # distance less 1000km
    def test_co2_to_less1000(self, Zurich: City, London: City):
        emit = 200
        distance = Zurich.distance_to(London)
        citizens = Zurich.citizens
        test_emit = emit * distance * citizens
        real_emit = Zurich.co2_to(London)
        assert int(test_emit) == int(real_emit)

    # distance between 1000 to 8000
    def test_co2_to_between_1000_8000(self, Zurich: City, Algiers: City):
        emit = 250
        distance = Zurich.distance_to(Algiers)
        citizens = Zurich.citizens
        test_emit = emit * distance * citizens
        real_emit = Zurich.co2_to(Algiers)
        assert int(test_emit) == int(real_emit)

    # distance between 1000 to 8000
    def test_co2_to_more8000(self, Zurich: City, Canberra: City):
        emit = 300
        distance = Zurich.distance_to(Canberra)
        citizens = Zurich.citizens
        test_emit = emit * distance * citizens
        real_emit = Zurich.co2_to(Canberra)
        assert int(test_emit) == int(real_emit)


#   negative tests
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
