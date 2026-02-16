# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401


def test_v1_geo_converter_kml_to_geo_json_get(client: TestClient):
    """Test case for v1_geo_converter_kml_to_geo_json_get

    Converts the KML file from the supplied URL to GeoJSON.
    """
    params = [("url", 'url_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/GeoConverter/KmlToGeoJson",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_geo_converter_kml_to_geo_json_post(client: TestClient):
    """Test case for v1_geo_converter_kml_to_geo_json_post

    Converts the KML provided as the body to GeoJSON.
    """
    params = [("body", 'body_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/GeoConverter/KmlToGeoJson",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_geo_converter_gpx_to_geo_json_get(client: TestClient):
    """Test case for v1_geo_converter_gpx_to_geo_json_get

    Converts the GPX file from the supplied URL to GeoJSON.
    """
    params = [("url", 'url_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/GeoConverter/GpxToGeoJson",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_geo_converter_gpx_to_geo_json_post(client: TestClient):
    """Test case for v1_geo_converter_gpx_to_geo_json_post

    Converts the GPX provided as the body to GeoJSON.
    """
    params = [("body", 'body_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/GeoConverter/GpxToGeoJson",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

