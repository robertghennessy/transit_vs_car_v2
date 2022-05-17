"""
Description: This file contains the functions that are used to collect transit data in the San Francisco
Bay Area by using 511 api.

@author: Robert Hennessy (robertghennessy@gmail.com)
"""
import requests
import json
import datetime as dt
import pandas as pd
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict


def query_gtfs_rt(transit_api_key: str, gtfs_rt_api_website: str, transit_agency: str) -> dict:
    """
    Query the San Francisco Bay Area 511 api to collect trip update information.

    :param transit_api_key: string that contains the api key for 511.org
    :type transit_api_key: str

    :param gtfs_rt_api_website: weblink to 511 api
    :type gtfs_rt_api_website: str

    :param transit_agency: string code for transit operator. Example: Caltrain = CT
    :type transit_agency: str

    :return dictionary with the stop monitoring information
    """
    feed = gtfs_realtime_pb2.FeedMessage()
    url = (gtfs_rt_api_website + transit_api_key + '&agency=' + transit_agency)
    response = requests.get(url)
    feed.ParseFromString(response.content)
    return MessageToDict(feed)


def query_siri_511(transit_api_key: str, siri_511_api_website: str, transit_agency: str) -> list:
    """
    Query the 511 api to collect stop monitoring information. Convert the json
        to a dict

    :param transit_api_key: string that contains the api key for 511.org
    :type transit_api_key: str

    :param siri_511_api_website: weblink to 511 api
    :type siri_511_api_website: str

    :param transit_agency: string code for transit operator. Example: Caltrain = CT
    :type transit_agency: str

    :return list with the stop monitoring information
    """
    url = (siri_511_api_website + transit_api_key + '&agency=' + transit_agency +
           '&Format=JSON')
    json_url = requests.get(url)
    data = json.loads(json_url.content.decode('utf-8-sig'))
    return data['ServiceDelivery']['StopMonitoringDelivery']['MonitoredStopVisit']
