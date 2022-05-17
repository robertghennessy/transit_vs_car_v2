"""
Description: This file contains a class for a Vehicle that contains real time information

@author: Robert Hennessy (robertghennessy@gmail.com)
"""


import numpy as np
import pandas as pd
import datetime as dt


class VehicleGTFSRT:
    def __init__(self, input_dict: dict):
        """
        Initialize the vehicle.

        :param input_dict: Dictionary that contains information for a vehicle.
        :type input_dict: dict
        """
        self.id = input_dict["id"]
        self.timestamp = dt.datetime.fromtimestamp(float(input_dict["tripUpdate"]["timestamp"]), dt.timezone.utc)
        self.utc_times = self.extract_times(input_dict["tripUpdate"]["stopTimeUpdate"])

    def extract_times(self, stop_time_updates: dict) -> pd.DataFrame:
        """
        Converts the stop times dictionary into a pandas dataframe.

        :param stop_time_updates: Dictionary that contains the real time stop information for a vehicle.
        :type stop_time_updates: dict

        :return: pandas dataframe that contains stop id, arrival time and departure time
        :rtype: DataFrame
        """
        stop_list = []
        for stop_update in stop_time_updates:
            departure_time = dt.datetime.fromtimestamp(float(stop_update["departure"]["time"]), dt.timezone.utc)
            if "arrival" in stop_update:
                arrival_time = dt.datetime.fromtimestamp(float(stop_update["arrival"]["time"]), dt.timezone.utc)
            else:
                arrival_time = np.NaN
            stop_list.append([stop_update["stopId"], arrival_time, departure_time])
        return pd.DataFrame(stop_list, columns=["StopId", "ArrivalTimeUTC", "DepartureTimeUTC"])


class VehicleSIRI:
    def __init__(self, input_dict: dict):
        """
        Initialize the vehicle.

        :param input_dict: Dictionary that contains information for a vehicle.
        :type input_dict: dict
        """
        self.id = input_dict["id"]
        self.timestamp = dt.datetime.utcfromtimestamp(float(input_dict["tripUpdate"]["timestamp"]))
        self.utc_times = self.extract_times(input_dict["tripUpdate"]["stopTimeUpdate"])

    def extract_times(self, vehicle_dict: dict) -> pd.DataFrame:
        """
        Converts vehicle dictionary into a pandas dataframe.

        """
