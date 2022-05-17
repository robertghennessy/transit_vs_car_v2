"""Tests for car_time file."""
import pytest
from transit_vs_car_v2 import transit_time_511
import configparser
import os

# import the configuration file which has the api keys
path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.abspath(os.path.join(path_current_directory, '..', 'config.ini'))
config = configparser.ConfigParser()
config.read(path_config_file)


def test_query_gtfs_rt():
    transit_api_key = config['keys']['Transit511Key']
    gtfs_rt_api_website = config['gtfs_rt_511']['gtfs_rt_api']
    transit_agency = config['gtfs_rt_511']['agency']
    output = transit_time_511.query_gtfs_rt(transit_api_key, gtfs_rt_api_website, transit_agency)
    assert type(output) == dict
    assert len(output) > 0

def test_query_siri_511():
    transit_api_key = config['keys']['Transit511Key']
    siri_rt_api_website = config['siri_511']['siri_511_api']
    transit_agency = config['siri_511']['agency']
    output = transit_time_511.query_siri_511(transit_api_key, siri_rt_api_website, transit_agency)
    assert type(output) == list
    assert len(output) > 0
