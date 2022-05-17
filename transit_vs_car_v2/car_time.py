"""
Description: This file contains the functions that are used to traffic data.

@author: Robert Hennessy (robertghennessy@gmail.com)
"""
import datetime as dt
import googlemaps

# @ten.retry(**RETRY_PARAMS)


def setup_google_api(api_key):
    """
    Creates client used to query google

    :param api_key: string that contains the Google api key
    :type api_key: str

    :return: google maps client
    :type: googlemaps.Client
    """
    return googlemaps.Client(key=api_key, timeout=5)


def query_google_api(google_client, start_loc, end_loc):
    """
    Queries the Google api to determine the driving time between
    the start and location. The retry wrapper will retry this function if
    an error occurs. The method is exponential back off with jitter, and it
    will retry 5 times before raising an exception.

    :param google_client: google client that is used to query directions
    :type google_client: googlemaps.Client()

    :param start_loc: dict that contains the latitude and longitude of the
        start station
    :type start_loc: dictionary

    :param end_loc: dict that contains the latitude and longitude of the
        start station
    :type end_loc: dictionary

    :duration_in_traffic: returns duration in traffic for the fastest route
    :rtype duration_in_traffic: float

    :directions_result: list of the routes
    :rtype directions_result: list

    """
    now = dt.datetime.now()
    # query Google Maps for the results
    directions_result = google_client.directions(start_loc,
                                                 end_loc,
                                                 mode="driving",
                                                 departure_time=now)
    # duration in traffic in seconds
    duration_in_traffic = (directions_result[0]['legs'][0][
        'duration_in_traffic']['value'])
    return duration_in_traffic, directions_result


def query_google_traffic(trip_index, trip_id, start_station, end_station,
                         start_loc, end_loc, sql_db_loc):
    """
    Not sure if this needs to be moved over from v1. Just gets the data, creates some data objects and saves data.
    I would consider clumping things together
    """

