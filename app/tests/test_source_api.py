# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.pgcrud_result import PGCRUDResult  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401
from openapi_server.models.source_linked import SourceLinked  # noqa: F401


def test_v1_source_get(client: TestClient):
    """Test case for v1_source_get

    GET Sources List
    """
    params = [("pagenumber", 1),     ("pagesize", 56),     ("language", 'language_example'),     ("idlist", 'idlist_example'),     ("typelist", 'typelist_example'),     ("fields", ['fields_example']),     ("searchfilter", 'searchfilter_example'),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False),     ("getasidarray", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Source",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_source_post(client: TestClient):
    """Test case for v1_source_post

    POST Insert new Source
    """
    source_linked = {"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"types":["Types","Types"],"description":{"key":"Description"},"self":"Self","url":"Url","name":{"key":"Name"},"interfaces":["Interfaces","Interfaces"],"sync_data_config":[{"base_url":"BaseUrl","path_param":["PathParam","PathParam"],"sync_data_api_url":"SyncDataApiUrl"},{"base_url":"BaseUrl","path_param":["PathParam","PathParam"],"sync_data_api_url":"SyncDataApiUrl"}],"first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"id":"Id","key":"Key"}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/Source",
    #    headers=headers,
    #    json=source_linked,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_source(client: TestClient):
    """Test case for single_source

    GET Source Single
    """
    params = [("language", 'language_example'),     ("fields", ['fields_example']),     ("localizationlanguage", 'localizationlanguage_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Source/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_source_id_put(client: TestClient):
    """Test case for v1_source_id_put

    PUT Modify existing Source
    """
    source_linked = {"license_info":{"license_holder":"LicenseHolder","closed_data":1,"license":"CC0","author":"Author"},"types":["Types","Types"],"description":{"key":"Description"},"self":"Self","url":"Url","name":{"key":"Name"},"interfaces":["Interfaces","Interfaces"],"sync_data_config":[{"base_url":"BaseUrl","path_param":["PathParam","PathParam"],"sync_data_api_url":"SyncDataApiUrl"},{"base_url":"BaseUrl","path_param":["PathParam","PathParam"],"sync_data_api_url":"SyncDataApiUrl"}],"first_import":"2000-01-23T04:56:07.000+00:00","last_change":"2000-01-23T04:56:07.000+00:00","_meta":{"type":"accommodation","last_update":"2000-01-23T04:56:07.000+00:00","id":"Id","source":"Source","reduced":1,"update_info":{"updated_by":"UpdatedBy","update_source":"UpdateSource","update_history":[{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"},{"updated_by":"UpdatedBy","last_update":"2000-01-23T04:56:07.000+00:00","update_source":"UpdateSource"}]}},"id":"Id","key":"Key"}

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/Source/{id}".format(id='id_example'),
    #    headers=headers,
    #    json=source_linked,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_source_id_delete(client: TestClient):
    """Test case for v1_source_id_delete

    DELETE Source by Id
    """

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/Source/{id}".format(id='id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

