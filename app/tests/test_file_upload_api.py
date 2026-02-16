# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from openapi_server.models.string_string_values_key_value_pair import StringStringValuesKeyValuePair  # noqa: F401


def test_v1_file_upload_post(client: TestClient):
    """Test case for v1_file_upload_post

     (Auth)
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    data = {
        "form": [openapi_server.StringStringValuesKeyValuePair()]
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/FileUpload",
    #    headers=headers,
    #    data=data,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_file_upload_image_post(client: TestClient):
    """Test case for v1_file_upload_image_post

     (Auth)
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    data = {
        "form": [openapi_server.StringStringValuesKeyValuePair()]
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/FileUpload/Image",
    #    headers=headers,
    #    data=data,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_file_delete_filepath_delete(client: TestClient):
    """Test case for v1_file_delete_filepath_delete

     (Auth)
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/FileDelete/{filepath}".format(filepath='filepath_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

