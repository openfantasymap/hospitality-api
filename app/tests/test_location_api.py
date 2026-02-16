# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.loc_helperclass import LocHelperclass  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401


def test_v1_location_get(client: TestClient):
    """Test case for v1_location_get

    GET Location List (Use in locfilter)
    """
    params = [("language", 'language_example'),     ("pagenumber", 56),     ("type", null),     ("showall", True),     ("locfilter", 'locfilter_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Location",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_location_skiarea_get(client: TestClient):
    """Test case for v1_location_skiarea_get

    GET Skiarea List (Use in locfilter as \"ska\")
    """
    params = [("language", 'language_example'),     ("pagenumber", 56),     ("locfilter", 'locfilter_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Location/Skiarea",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

