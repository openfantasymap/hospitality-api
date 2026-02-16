# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.json_raw import JsonRaw  # noqa: F401
from openapi_server.models.problem_details import ProblemDetails  # noqa: F401


def test_v1_find_get(client: TestClient):
    """Test case for v1_find_get

    GET Search over all Entities
    """
    params = [("term", 'term_example'),     ("language", 'en'),     ("odhtype", 'odhtype_example'),     ("type", 'type_example'),     ("searchbasetext", False),     ("filteronfields", ['filteronfields_example']),     ("locfilter", 'locfilter_example'),     ("fields", ['fields_example']),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("limitto", 5),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Find",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_v1_filter_get(client: TestClient):
    """Test case for v1_filter_get

    GET Search over all Entities
    """
    params = [("term", 'term_example'),     ("language", 'en'),     ("odhtype", 'odhtype_example'),     ("type", 'type_example'),     ("searchbasetext", False),     ("filteronfields", ['filteronfields_example']),     ("locfilter", 'locfilter_example'),     ("fields", ['fields_example']),     ("rawfilter", 'rawfilter_example'),     ("rawsort", 'rawsort_example'),     ("limitto", 5),     ("removenullvalues", False)]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/Filter",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

