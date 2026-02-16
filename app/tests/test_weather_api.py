# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.bezirks_weather import BezirksWeather  # noqa: F401
from openapi_server.models.measuringpoint_v2 import MeasuringpointV2  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401
from openapi_server.models.snow_report_base_data import SnowReportBaseData  # noqa: F401
from openapi_server.models.weather import Weather  # noqa: F401
from openapi_server.models.weather_forecast_linked import WeatherForecastLinked  # noqa: F401
from openapi_server.models.weather_history import WeatherHistory  # noqa: F401
from openapi_server.models.weather_real_time import WeatherRealTime  # noqa: F401


def test_v1_weather_get(client: TestClient):
    """Test case for v1_weather_get

    GET Current Suedtirol Weather LIVE
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("language", 'en'),     ("locfilter", 'locfilter_example'),     ("extended", True),     ("source", 'source_example'),     ("fields", ['fields_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_weather(client: TestClient):
    """Test case for single_weather

    GET Current Suedtirol Weather LIVE Single
    """
    params = [("language", 'en'),     ("source", 'source_example'),     ("fields", ['fields_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_weather_history_get(client: TestClient):
    """Test case for v1_weather_history_get

    GET Suedtirol Weather HISTORY
    """
    params = [("pagenumber", 1),     ("pagesize", 56),     ("language", 'language_example'),     ("idlist", 'idlist_example'),     ("locfilter", 'locfilter_example'),     ("datefrom", 'datefrom_example'),     ("dateto", 'dateto_example'),     ("seed", 'seed_example'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("lastchange", 'lastchange_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/WeatherHistory",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_weather_history(client: TestClient):
    """Test case for single_weather_history

    GET Suedtirol Weather HISTORY SINGLE
    """
    params = [("language", 'language_example'),     ("fields", ['fields_example']),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/WeatherHistory/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_weather_district_get(client: TestClient):
    """Test case for v1_weather_district_get

    GET District Weather LIVE
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("locfilter", 'locfilter_example'),     ("language", 'en'),     ("source", 'source_example'),     ("fields", ['fields_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather/District",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_weather_district(client: TestClient):
    """Test case for single_weather_district

    GET District Weather LIVE SINGLE
    """
    params = [("language", 'en'),     ("source", 'source_example'),     ("fields", ['fields_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather/District/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_weather_realtime_get(client: TestClient):
    """Test case for v1_weather_realtime_get

    GET Current Realtime Weather LIVE
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("language", 'en'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("fields", ['fields_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather/Realtime",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_weather_realtime(client: TestClient):
    """Test case for single_weather_realtime

    GET Current Realtime Weather LIVE Single
    """
    params = [("language", 'en'),     ("fields", ['fields_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather/Realtime/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_weather_forecast_get(client: TestClient):
    """Test case for v1_weather_forecast_get

    GET Weather Forecast
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("locfilter", 'locfilter_example'),     ("language", 'en'),     ("fields", ['fields_example']),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather/Forecast",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_weather_forecast(client: TestClient):
    """Test case for single_weather_forecast

    GET Weather Forecast Single
    """
    params = [("language", 'en'),     ("fields", ['fields_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather/Forecast/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_weather_measuringpoint_get(client: TestClient):
    """Test case for v1_weather_measuringpoint_get

    GET Measuringpoint LIST
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("locfilter", 'locfilter_example'),     ("tagfilter", 'tagfilter_example'),     ("areafilter", 'areafilter_example'),     ("skiareafilter", 'skiareafilter_example'),     ("language", 'language_example'),     ("source", 'source_example'),     ("active", True),     ("publishedon", 'publishedon_example'),     ("updatefrom", 'updatefrom_example'),     ("latitude", 'latitude_example'),     ("longitude", 'longitude_example'),     ("radius", 'radius_example'),     ("polygon", 'polygon_example'),     ("seed", 'seed_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather/Measuringpoint",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_weather_measuringpoint(client: TestClient):
    """Test case for single_weather_measuringpoint

    GET Measuringpoint SINGLE
    """
    params = [("language", 'language_example'),     ("fields", ['fields_example']),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather/Measuringpoint/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_weather_snow_report_get(client: TestClient):
    """Test case for v1_weather_snow_report_get

    GET Snowreport Data LIVE
    """
    params = [("pagenumber", 56),     ("pagesize", 56),     ("skiareaid", 'skiareaid_example'),     ("lang", 'en')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather/SnowReport",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_weather_snow_report(client: TestClient):
    """Test case for single_weather_snow_report

    GET Snowreport Data LIVE Single
    """
    params = [("lang", 'en')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Weather/SnowReport/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

