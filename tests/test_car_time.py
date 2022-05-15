"""Tests for car_time file."""
import googlemaps
import pytest
from transit_vs_car_v2 import car_time
import configparser
import os

# import the configuration file which has the api keys
path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.abspath(os.path.join(path_current_directory, '..', 'config.ini'))
config = configparser.ConfigParser()
config.read(path_config_file)


def test_setup_google_api():
    assert isinstance(car_time.setup_google_api(config['keys']['googleapi']),
                      googlemaps.Client)


def test_query_google_api():
    start_loc = dict(lat=37.486159, lng=-122.231936)
    end_loc = dict(lat=37.568087, lng=-122.323851)
    google_client = car_time.setup_google_api(config['keys']['googleapi'])
    duration_in_traffic, directions_result = \
        car_time.query_google_api(google_client, start_loc, end_loc)
    assert type(directions_result) == list
    assert len(directions_result) > 0 # nonempty
    assert duration_in_traffic >= 0
