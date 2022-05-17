"""Tests for car_time file."""
import pytest
from transit_vs_car_v2 import vehicle
import datetime as dt
import pandas as pd
import numpy as np


def test_vehicle_complete():
    test_vehicle_dict = {"id": "244", "tripUpdate": {"timestamp": "1652652590", "stopTimeUpdate": [
       {"arrival": {"time": "1652652561"}, "departure": {"time": "1652652690"}, "stopId": "70202"},
       {"arrival": {"time": "1652652722"}, "departure": {"time": "1652652975"}, "stopId": "70212"}]}}
    test_vehicle = vehicle.VehicleGTFSRT(test_vehicle_dict)
    assert test_vehicle.id == "244"
    assert test_vehicle.timestamp == dt.datetime.fromtimestamp(float(1652652590), dt.timezone.utc)
    stop_list = [["70202", dt.datetime.fromtimestamp(float(1652652561), dt.timezone.utc),
                  dt.datetime.fromtimestamp(float(1652652690), dt.timezone.utc)],
                 ["70212", dt.datetime.fromtimestamp(float(1652652722), dt.timezone.utc),
                  dt.datetime.fromtimestamp(float(1652652975), dt.timezone.utc)]]
    tst_df = pd.DataFrame(stop_list, columns=["StopId", "ArrivalTimeUTC", "DepartureTimeUTC"])
    assert tst_df.equals(test_vehicle.utc_times)


def test_vehicle_missing_arrival():
    test_vehicle_dict = {"id": "244", "tripUpdate": {"timestamp": "1652652590", "stopTimeUpdate": [
        {"arrival": {"time": "1652652561"}, "departure": {"time": "1652652690"}, "stopId": "70202"},
        {"departure": {"time": "1652652975"}, "stopId": "70212"}]}}
    test_vehicle = vehicle.VehicleGTFSRT(test_vehicle_dict)
    df = test_vehicle.utc_times
    assert df[df['StopId'] == '70212']['ArrivalTimeUTC'].isnull().values[0]
