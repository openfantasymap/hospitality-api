# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401
from openapi_server.models.push_response import PushResponse  # noqa: F401


def test_v1_push_response_get(client: TestClient):
    """Test case for v1_push_response_get

    GET PushResponse List
    """
    params = [("pagenumber", 1),     ("pagesize", 56),     ("idlist", 'idlist_example'),     ("publisher", 'publisher_example'),     ("begindate", 'begindate_example'),     ("enddate", 'enddate_example'),     ("objectidlist", 'objectidlist_example'),     ("objecttypelist", 'objecttypelist_example'),     ("latest", True),     ("fields", ['fields_example']),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/PushResponse",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_single_push_response(client: TestClient):
    """Test case for single_push_response

    GET PushResponse Single
    """
    params = [("fields", ['fields_example']),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/PushResponse/{id}".format(id='id_example'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_push_response_search_post(client: TestClient):
    """Test case for v1_push_response_search_post

    
    """
    request_body = [None]

    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/PushResponseSearch",
    #    headers=headers,
    #    json=request_body,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

